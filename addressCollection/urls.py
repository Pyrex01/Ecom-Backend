from django.urls import path
from addressCollection.views import *
urlpatterns = [
    path("getAddress/",getAddress,name="it will send address"),
    path("setAddress/",setAddress,name="it will resive address")
]