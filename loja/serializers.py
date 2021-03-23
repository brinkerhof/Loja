from rest_framework import serializers
from loja.models import Shirt

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shirt
        fields = '__all__'
