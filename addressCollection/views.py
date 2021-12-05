from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.authentication import TokenAuthentication
from addressCollection.models import *
from addressCollection.serializers import *
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(methods=['get'],
operation_description="When user is loged in it returns all addresses of user",
responses={200:"returns all the address user currently having",404:"user not loged in or user is not having any address"})
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def getAddress(request):
    try:
        address = Address.objects.filter(User_ID=request.user)
        address = AdressSerialized(address,many=True)
        print(address.data,"====================================================")
        return Response(data=address.data,status=status.HTTP_200_OK)
    except Address.DoesNotExist as E:
        return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(methods=['post'],
operation_description="When user is loged in it returns all addresses of user",
responses={200:"returns all the address user currently having",404:"user not loged in or user is not having any address"})
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def setAddress(request):
    user = request.user
    state = request.GET["state"]
    name = request.GET["name"]
    Phone_number= request.GET["Phone_number"]
    pincode = request.GET["pincode"]
    regien = request.GET["regien"]
    landmark = request.GET["landmark"]
    town = request.GET["town"]
    address_type = Address_types.objects.get(pk=request.GET["address_type"])
    Address(Name=name,
    State=state,
    Phone_number=Phone_number,
    Pincode=pincode,
    Regein=regien,
    Landmark=landmark,
    Address_type_ID=address_type,
    Town=town,
    User_ID=user).save()
    return Response(status=status.HTTP_202_ACCEPTED)

