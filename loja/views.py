from django.shortcuts import render
from rest_framework import views, viewsets
from loja.models import Shirt
from loja.serializers import ShirtSerializer

class ShirtsViewSet(viewsets.ModelViewSet):
    """Vai te fude CDK"""
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer
