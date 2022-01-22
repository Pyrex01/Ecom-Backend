from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from store.models import Cart, Items


class ItemsInList(ModelSerializer):
    class Meta:
        model = Items
        fields = ["id","Name","Price","Display_Image"]


class SingleItem(ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"



class CartItems(ModelSerializer):
    Items_ID = ItemsInList()
    class Meta:
        model = Cart
        fields = ["Quantity","Items_ID"]


