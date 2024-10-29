# Register your models here.

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_100g', 'price_4L', 'price_6L', 'stock_100g', 'stock_4L', 'stock_6L')
    fields = ('name', 'description', 'image', 'price_100g', 'price_4L', 'price_6L', 'stock_100g', 'stock_4L', 'stock_6L')

    search_fields = ('name',)
    list_filter = ('name',)
    
admin.site.register(Product, ProductAdmin)
