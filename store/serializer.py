from rest_framework.serializers import ModelSerializer
from store.models import Cart, Items, Orders
from addressCollection.serializers import AdressSerialized

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

class orderSerializer(ModelSerializer):
    Items_ID = ItemsInList()
    Shipping_Address = AdressSerialized()
    Billing_Address = AdressSerialized()
    class Meta:
        model = Orders
        fields = ["Status","First_Name","Last_Name","Phone_Number","Items_ID","Order_date","Quantity","Tracking_ID","Shipping_Address","Billing_Address"]
