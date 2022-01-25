from django.urls import path
from store.views import *

urlpatterns = [
    path("getItems/",getItems.as_view()),
    path("getSortItems/",getSortItems.as_view()),
    path("getitem/",getItem,name="single Item"),
    path("order/",doOrder,name="order taken here"),
    path("getItemsInCart/",getItemsInCart,name="all items in user cart"),
    path("setItemsInCart/",addtoCart,name="all items in user cart"),
    path("getallOrders/",getOrders,name="all items in user cart"),
    path("checkout/",checkOUtCart,name="all items in user cart"),
    path("updataQuantitiy/",changeQuantitiy,name="all items in user cart"),
]