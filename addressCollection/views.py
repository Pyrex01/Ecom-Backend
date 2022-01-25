from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.authentication import TokenAuthentication
from addressCollection.models import *
from addressCollection.serializers import *
from drf_yasg.utils import swagger_auto_schema
from userManagement.models import Users
from drf_yasg.openapi import Parameter






@swagger_auto_schema(methods=['get'],
operation_description="When user is loged in it returns all addresses of user",
responses={200:"returns all the address user currently having",404:"user not loged in or user is not having any address"})
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def getAddress(request):
    try:
        address = Address.objects.filter(User_ID=request.user)
        address = AdressSerialized(address,many=True)
        return Response(data=address.data,status=status.HTTP_200_OK)
    except Address.DoesNotExist as E:
        return Response(status=status.HTTP_404_NOT_FOUND)







@swagger_auto_schema(methods=['post'],
operation_description="send value here as mentioned to add users address on data base to order stuff",
manual_parameters=[
            Parameter("state","in request",description= """
            ('AP',"Andhra Pradesh"),
            ('AR',"Arunachal Pradesh"),
            ('AS',"Assam"),
            ('BR',"Bihar"),
            ('CT',"Chhattisgarh"),
            ('GA',"Goa"),
            ('GJ',"Gujarat"),
            ('HR',"Haryana"),
            ('HP',"Himachal Pradesh"),
            ('JH',"Jharkhand"),
            ('KA',"Karnataka"),
            ('KL',"Kerala"),
            ('MP',"Madhya Pradesh"),
            ('MH',"Maharashtra"),
            ('MN',"Manipur"),
            ('ML',"Meghalaya"),
            ('MZ',"Mizoram"),
            ('NL',"Nagaland"),
            ('OR',"Orissa, Odisha"),
            ('PB',"Punjab, Punjab (India)"),
            ('RJ',"Rajasthan"),
            ('SK',"Sikkim"),
            ('TN',"Tamil Nadu, Tamizh Nadu"),
            ('TG',"Telangana"),
            ('TR',"Tripura"),
            ('UL',"Uttarakhand"),
            ('UP',"Uttar Pradesh"),
            ('WB',"West Bengal"),
            ('AN',"Andaman and Nicobar Islands"),
            ('CH',"Chandigarh"),
            ('DN',"Dadra and Nagar Haveli, Dadra & Nagar Haveli"),
            ('DD',"Daman and Diu"),
            ('DL',"Delhi, National Capital Territory of Delhi"),
            ('JK',"Jammu and Kashmir"),
            ('LA',"Ladakh"),
            ('LD',"Lakshadweep"),
            ('PY',"Pondicherry, Puducherry"),
            
            send only that two word short form for state
            """,type="string",required=True),
            Parameter("name","in request","whatever user name this address for its own identifications",True,type="string"),
            Parameter("Phone_number","in request","",True,type="integer | string"),
            Parameter("pincode","in request","",True,type="integer | string"),
            Parameter("regien","in request","apologies but I dont know how to write regien under stand it",True,type="string"),
            Parameter("landmark","in request","*optional",False,type="string"),
            Parameter("town","in request","",True,type="string"),
            Parameter("address_type","in request","address_type can only be \"home\" or \"office\" as mentioned in",True,type="string"),
            ],
responses={202:"returns nothign which means its accepted",400:"bad request"})
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def setAddress(request):
    state = request.data["state"]
    name = request.data["name"]
    Phone_number= request.data["Phone_number"]
    pincode = request.data["pincode"]
    regien = request.data["regien"]
    landmark = request.data["landmark"]
    town = request.data["town"]
    address_type = Address_types.objects.get(Address_type=request.data["address_type"])
    Address(
    Name=name,
    State=state,
    Phone_number=Phone_number,
    Pincode=pincode,
    Regein=regien,
    Landmark=landmark,
    Address_type_ID=address_type,
    Town=town,
    User_ID=request.user).save()
    return Response(status=status.HTTP_202_ACCEPTED)

