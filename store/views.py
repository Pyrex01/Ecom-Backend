from rest_framework import status
from rest_framework.generics import ListAPIView
from store.pagination import ListPage ,ListPageSort
from store.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view ,authentication_classes
from rest_framework.response import Response
from store.serializer import CartItems, ItemsInList , SingleItem, orderSerializer
from addressCollection.models import Address
import random
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg.openapi import Parameter
from django.db.models import F
from userManagement.models import *
from django.core import mail
from django.conf.global_settings import EMAIL_HOST_USER

class getItems(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsInList
    pagination_class = ListPage
class getSortItems(ListAPIView):
    queryset = Items.objects.all()
    queryset = queryset.exclude(Quantity=0)
    serializer_class = ItemsInList
    pagination_class = ListPageSort

    @swagger_auto_schema(method='get',
    operation_description="this is to get single item with all its detail to show user ",
    manual_parameters= [
        Parameter('categories', "in request",'sort by categorie',type='string'),
        Parameter('sub_categorie', "in request",'sort by sub-categorie',type='string'),
        Parameter('searchString', "in request",'it will search for anything that has that name in it and return',type='string'),
        Parameter('Price', "in request",'this is for sort by price possible option is -1 for low to high 1 for high to low ',type='integer'),
        ],
    require=True,
    responses={200:ItemsInList(many=True),404:"no product available with this sort",400:"bad request"})
    @action(methods=['get'],detail=False)
    def get(self,request,**kwargs):
        return super().get(request,**kwargs)

    def get_queryset(self):
        queryset = Items.objects.all()
        data = self.request.GET
        keys = data.keys()
        if "searchString" in keys:
            queryset = queryset.filter(Name__icontains=data["searchString"])
        if "categories" in keys:
            sub = Belongs.objects.filter(Categorie_ID=data["categories"])
            print("sub",sub)
            queryset = queryset.filter(Belongs_ID__in=sub)
        if "sub_categorie"in keys:
            queryset = queryset.filter(Belongs_ID=data["sub_categorie"])
        if "by_price" in keys:
            if data["by_price"]==1:
                queryset = queryset.order_by("Price")
            if data["by_price"]==-1:
                queryset = queryset.order_by("-Price")
        return queryset


@swagger_auto_schema(method='get',
    operation_description="this is to get single item with all its detail to show user ",
    manual_parameters= [Parameter('product_ID', "in request",'unique id of product slected by user to view', 
    type='interger')],
    require=True,
    responses={200:SingleItem(many=True),400:"item does not exist"})
@api_view(['GET'])
def getItem(request):
    try:
        item = Items.objects.get(pk=request.GET["product_ID"])
        item = SingleItem(item)
        return Response(data=item.data,status=200)
    except Items.DoesNotExist as E:
        return Response(status=404)


@swagger_auto_schema(operation_description="for users to place order they must be loged in",method='post',
    manual_parameters=[ Parameter("itemID","in request","item's id selected by user",type="integer",required=True),
                        Parameter("quantity","in request","how many amount of item by user to order",type="integer",required=True),
                        Parameter("shippingID","in request","out of all user addresses whatever user selects its ID",type="integer",required=True),
                        Parameter("billingID","in request","out of all user addresses whatever user selects its ID",type="integer",required=True),
                        Parameter("First_Name","in request","receivers first name",type="integer",required=True),
                        Parameter("Last_Name","in request","receivers last name",type="integer",required=True),
                        Parameter("Phone_Number","in request","phone number of reciever",type="integer",required=True)],
    responses={200:"order placed",400:"bad request or quantitiy is not that much"})
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def doOrder(request):
    item = Items.objects.get(pk=request.data["itemID"])
    quantity = request.data["quantity"]
    First_Name = request.data["First_Name"]
    Last_Name = request.data["Last_Name"]
    Phone_Number = request.data["Phone_Number"]
    if item.Quantity < int(quantity):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    shipping = request.data["shippingID"]
    billing = request.data["billingID"]

    item.Quantity -= quantity
    item.save()
    Orders(
    Items_ID=item,
    Customers_ID=request.user,
    Quantity=quantity,
    Tracking_ID=random.randint(222,999),
    Shipping_Address=Address.objects.get(pk=shipping),
    Billing_Address=Address.objects.get(pk=billing),
    First_Name=First_Name,
    Last_Name=Last_Name,
    Phone_Number=Phone_Number
    ).save()
    email = mail.send_mail("Confirmation for orders placed",f"hello {request.user.First_Name} the item you want to buy is successfully placed in order order--{item.Name}")
    email.send(fail_silently=False)
    return Response(status=status.HTTP_200_OK)



@swagger_auto_schema(operation_description="users must be logged in to get cart items for that user must send signup token in header",
method='get',responses={200:CartItems(many=True),500:"something went wrong",401:"un authorized token not recieved"})
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def getItemsInCart(request):
    listOfItems = Cart.objects.filter(User_ID=request.user.id,Quantity_gt=0)
    serialized = CartItems(listOfItems,many=True)
    return Response(data=serialized.data,status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="complete check out of cart list",method='post',
    manual_parameters=[
        Parameter("first_name","in request",required=True,type="string"),
        Parameter("last_name","in request",required=True,type="string"),
        Parameter("Phone_number","in request",required=True,type="string"),
        Parameter("shipping_address_id","in request",required=True,type="string|integer"),
        Parameter("billing_address_id","in request",required=True,type="string|integer"),
    ],
    responses={202:"all orders places success fully",404:"some items not available in that quantity or items id wrong",400:"bad request",500:"something went wrong with server"}
)
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def checkOUtCart(request):
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    Phone_number = request.data["Phone_number"]
    shipping_address = request.data["shipping_address_id"]
    billing_address = request.data["billing_address_id"]
    allCart = Cart.objects.filter(User_ID=request.user.id)
    for cart in allCart:
        
        if (cart.Items_ID.Quantity-cart.Quantity) < 0:
            return Response(data={"items not available in that quantitiy":cart.Items_ID.Name},status=status.HTTP_404_NOT_FOUND)
        Orders(First_Name=first_name,
        Last_Name=last_name,
        Phone_Number=Phone_number,
        Items_ID=cart.Items_ID,
        Customers_ID=request.user,
        Quantity=cart.Quantity,
        Tracking_ID=random.randint(999999,9999999999),
        Shipping_Address=Address.objects.get(pk=shipping_address),
        Billing_Address=Address.objects.get(pk=billing_address)).save()
        cart.Items_ID.Quantity -= cart.Quantity
        cart.Items_ID.save()
        cart.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
    




@swagger_auto_schema(operation_description="for users to place order they must be loged in",method='get',
    manual_parameters=[ Parameter("itemID","in request","item's id selected by user",type="integer",required=True),
                        Parameter("quantity","in request","item's id selected by user",type="integer",required=True),],
    responses={200:"order placed",400:"bad request or quantitiy is not that much"})
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def addtoCart(request):
    try:
        cartob=Cart.objects.get(User_ID=request.user,Items_ID=Items.objects.get(pk=request.GET["itemID"]))
        cartob.Quantity = cartob.Quantity + int(request.GET["quantity"])
        cartob.save()
        return Response(status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        Cart(User_ID=Users.objects.get(pk=request.user.id),
        Items_ID=Items.objects.get(pk=request.GET["itemID"]),
        Quantity=request.GET["quantity"]).save()
        return Response(status=status.HTTP_200_OK)



@swagger_auto_schema(operation_description="get all the orders done by users here user must be logged in thourgh and sent token through header",
method='get',responses={200:orderSerializer(many=True),500:"something went wrong with server",400:"bad request",403:"not authenticated"})
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def getOrders(request):
    orders = Orders.objects.filter(Customers_ID=request.user.id)
    serislizedOrder = orderSerializer(orders,many=True)
    return Response(data=serislizedOrder.data,status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description="update quantitiy in cart of user of single item",
method='post',
manual_parameters=[
    Parameter("cartID","in POST",required=True,type="string|integer"),
    Parameter("quantity","in POST",required=True,type="string|integer")
],
responses={202:"quantitiy updated",400:"bad request",500:"something went wrong with server"}
)
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def changeQuantitiy(request):
    cart_ID =request.data["cartID"]
    quantiy =request.data["quantity"]
    cart = Cart.objects.get(User_ID=request.user.id,pk=cart_ID)
    cart.Quantity = quantiy
    cart.save()
    return Response(status=status.HTTP_202_ACCEPTED)

