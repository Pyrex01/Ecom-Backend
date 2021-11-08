from django.urls import path
from store.views import *

urlpatterns = [
    path("getItems/",getItems.as_view()),
    path("getSortItems/",getSortItems.as_view()),
    path("getitem/",getItem,name="single Item"),
    path("order/",doOrder,name="order taken here")
]