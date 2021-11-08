from rest_framework.serializers import ModelSerializer
from addressCollection.models import Address , Address_types

class AdressSerialized(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"