from django.urls import path
from addressCollection.views import *
urlpatterns = [
    path("getAddress/",getAddress,name="it will resive address")
]