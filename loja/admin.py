from django.contrib import admin
from loja.models import Shirt

class Shirts(admin.ModelAdmin):
    list_display= ('id', 'name', 'price', 'new')
    list_display_links= ('id', 'name')
    search_fields= ('nome',)

admin.site.register(Shirt, Shirts)