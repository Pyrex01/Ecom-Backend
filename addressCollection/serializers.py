from rest_framework.serializers import ModelSerializer
from addressCollection.models import Address , Address_types


class AddtypesSerializer(ModelSerializer):
    class Meta:
        model = Address_types
        fields = ["Address_type"]

class AdressSerialized(ModelSerializer):
    Address_type_ID = AddtypesSerializer()
    class Meta:
        model = Address
        fields = "__all__"




