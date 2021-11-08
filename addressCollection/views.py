from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.authentication import TokenAuthentication
from addressCollection.models import *
from addressCollection.serializers import *



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

