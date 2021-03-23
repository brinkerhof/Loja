from django.contrib import admin
from django.urls import path, include
from loja.views import ShirtsViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register('shirts', ShirtsViewSet, basename='Shirts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
