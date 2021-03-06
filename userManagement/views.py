from os import stat
from drf_yasg.openapi import Parameter
from inflection import parameterize
from rest_framework.decorators import api_view , authentication_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.core import mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from .models import *
from drf_yasg.utils import swagger_auto_schema
import random
from datetime import datetime


@swagger_auto_schema(
    method = 'post',
    operation_description="this end point to take users data and create a unverified user",
    manual_parameters=[ 
        Parameter("First_Name","in request",type="string",required=True),
        Parameter("Second_Name","in request",type="string",required=True),
        Parameter("Email","in request",type="string",required=True),
        Parameter("password","in request",type="string",required=True),
        Parameter("Gender","in request","1 for male 2 for female and more to come",type="integer",required=True),
        Parameter("Phone","in request",type="integer | string"),
        Parameter("Photo","in request","photo should come in base 64 format of string",type="string")],
    responses={201:"user created and OTP is sent",226:"user with same email already exist",400:"bad request"})
@api_view(['POST'])
def signup(request):
    try:
        Users.objects.get(Email=request.data["Email"])
        return Response(data={"Email already in use"},status=status.HTTP_226_IM_USED)
    except Users.DoesNotExist:
        request.data["password"]= make_password(request.data["password"])
        request.data["Gender"] = Gender.objects.get(pk=request.data["Gender"])
        
        user = UnVerifiedUser(**request.data)
        user.OTP=random.randint(99999,999999)
        print("------------------------------------ OTP:",user.OTP,"----------------------------")
        html_content = render_to_string("userManagement/otptemp.html",{"OTP":user.OTP,"email":user.Email})
        content = strip_tags(html_content)
        email = mail.EmailMultiAlternatives(subject="Shoping Bazar Email Verification",from_email=EMAIL_HOST_USER,to=[user.Email],body=content)
        email.attach_alternative(html_content,"text/html")
        email.send(fail_silently=False)
        user.save()
        return Response(data={"signup_token":str(user.id)},status=status.HTTP_201_CREATED)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method = 'post',
    operation_description="this end point marks user as verified",
    manual_parameters=[ 
        Parameter("token","in request","token that recieved while signing up",type="UUID | string",required=True),
        Parameter("otp","in request","otp that has been mailed taken from user",type="integer | string",required=True)],
    responses={202:"user has been verified",400:"eithor of requiered paramenters missing or wrong request",410:"otp expired",404:"unvierified user got deleted or it never existed"})
@api_view(['POST'])
def confirmOTP(request):
    try:
        user = UnVerifiedUser.objects.get(id=request.data["token"],OTP=request.data["otp"])
        if user.Generated_Date.minute + 2 < datetime.now().minute:
            return Response(status=status.HTTP_410_GONE)
        cuser = Users(First_Name=user.First_Name,Second_Name=user.Second_Name,Email=user.Email,Gender=user.Gender,Photo=user.Photo,password=user.password)
        cuser.save()
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    except UnVerifiedUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except KeyError as e:
        return Response(data={"wrong info"},status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method = 'post',
    operation_description="this end point to login user with auth token",
    manual_parameters=[ 
        Parameter("Email","in request","Registered email with user",type="string",required=True),
        Parameter("password","in request","users password",type="string",required=True)],
    responses={202:"login success full with data of user and token key",403:"username or password incorrect",400:"bad request"})
@api_view(["POST"])
def login(request):
    try:
        user = Users.objects.get(Email=request.data["Email"])
        if user.check_password(request.data["password"]):
            token = Token.objects.get_or_create(user=user)[0]
            data = {"login_token":token.key,"First_name":user.First_Name,"Second_Name":user.Second_Name,"Photo":user.Photo}
            return Response(data=data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    except KeyError as E:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    except Exception as E:
        return Response(data="wrong info",status=status.HTTP_403_FORBIDDEN)

@swagger_auto_schema(
    method = 'post',
    operation_description="this end point to logout user with auth token",
    manual_parameters=[ 
        Parameter("Authorization : Token `key`","in header","loged in users token must be sent here",type="string",required=True)],
    responses={200:"success fully loged out !",400:"bad request"})
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def logout(request):
    print(request)
    try:
        print(request.user.id)
        Token.objects.get(user = request.user.id).delete()
        return Response(status=status.HTTP_200_OK)
    except Token.DoesNotExist as E:
        return Response(status=status.HTTP_404_NOT_FOUND)
        


@swagger_auto_schema(method='post',operation_description="send users complain to this url" , manual_parameters=[
    Parameter("description","in requst","users description here",True,type="string"),
    Parameter("title","in request","titile of description that problem is releted to more like subject in mail",True,type="string")],
    responses={200:"success fully complaint",400:"bad request",500:"something went wrong in server"})
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def getComplaint(request):
    Complaints(User=request.user,Description=request.data["description"],Title=request.data["title"]).save()
    return Response(status=status.HTTP_200_OK)




# mail.EmailMessage(subject="Django Otp verification",body='''<div style="flex:inline;"><h1>you have requested otp</h1> <div style="width:10px; height:10px;background:rgb(202, 235, 16);text:white"> 99999 </div> </div>''',from_email=EMAIL_HOST_USER,to=["khanshafique.ahamed@gmail.com"]).send(fail_silently=False)