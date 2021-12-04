from typing import Tuple
from pkg_resources import require
from rest_framework import status
from rest_framework.generics import ListAPIView
from store.pagination import ListPage
from store.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.response import Response
from store.serializer import ItemsInList , SingleItem
from addressCollection.models import Address
import random
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter

class getItems(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsInList
    pagination_class = ListPage

class getSortItems(ListAPIView):
    queryset = Items.objects.all()
    queryset = queryset.exclude(Quantity=0)
    serializer_class = ItemsInList
    pagination_class = ListPage
    def get_queryset(self):
        queryset = Items.objects.all()
        data = self.request.GET
        if "categories" in data.keys():
            sub = Belongs.objects.get(Categorie_ID=data["categories"])
            queryset = queryset.filter(Belongs_ID__in=sub)
        if "sub_categorie"in data.keys():
            queryset = queryset.filter(Belongs_ID=data["sub_categorie"])
        if "by_price" in data.keys():
            if data["by_price"]==1:
                queryset = queryset.order_by("Price")
            if data["by_price"]==0:
                queryset = queryset.order_by("-Price")
        return queryset

@swagger_auto_schema(method='get',
operation_description="this is to get single item with all its detail to show user ",
manual_parameters= [Parameter('product_ID', "in request",'unique id of product slected by user to view', 
type='interger')],
require=True,
responses={200:"returns product with all its details to show",400:"item does not exist"})
@api_view(['GET'])
def getItem(request):
    try:
        item = Items.objects.get(pk=request.GET["product_ID"])
        item = SingleItem(item)
        return Response(data=item.data,status=200)
    except Items.DoesNotExist as E:
        return Response(status=404)








@swagger_auto_schema(operation_description="for users to place order they must be loged in",method='get',
manual_parameters=[ Parameter("itemID","in request","item's id selected by user",type="integer",required=True),
                    Parameter("quantity","in request","how many amount of item by user to order",type="integer",required=True),
                    Parameter("addressID","in request","out of all user addresses whatever user selects its ID",type="integer",required=True)],
responses={200:"order placed",400:"bad request or quantitiy is not that much"})
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def doOrder(request):
    item = Items.objects.get(pk=request.GET["itemID"])
    quantity = request.GET["quantity"]
    if item.Quantity < quantity:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    address = request.GET["addressID"]
    item.Quantity = item.Quantity = quantity
    item.save()
    Orders(Items_ID=item,Customers_ID=request.user,Quantity=quantity,Tracking_ID=random.randint(222,999),Address_ID=Address.objects.get(pk=address)).save()
    return Response(status=status.HTTP_200_OK)



