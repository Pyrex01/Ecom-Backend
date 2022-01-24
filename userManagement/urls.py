from django.urls import path
from .views import *
urlpatterns = [
    path("signup/",signup,name="signup"),
    path('confirm/',confirmOTP,name="OTP confirm"),
    path('login/',login,name="token login"),
    path('logout/',logout,name="logout using token"),
    path('complaint/',getComplaint,name="register complaints here")
]