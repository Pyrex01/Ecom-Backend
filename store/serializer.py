from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from store.models import Items


class ItemsInList(ModelSerializer):
    class Meta:
        model = Items
        fields = ["id","Name","Price","Display_Image"]


class SingleItem(ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"