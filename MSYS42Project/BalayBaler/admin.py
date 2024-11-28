# Register your models here.

from django.contrib import admin
from .models import Product, Customer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_100g', 'price_4L', 'price_6L', 'stock_100g', 'stock_4L', 'stock_6L')
    fields = ('name', 'description', 'image', 'price_100g', 'price_4L', 'price_6L', 'stock_100g', 'stock_4L', 'stock_6L')

    search_fields = ('name',)
    list_filter = ('name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cart', 'fname', 'lname', 'phnum', 'email', 'mode', 'add1', 'add2', 'city', 'region', 'zip', 'delivery', 'specints')
    fields = ('cart', 'fname', 'lname', 'phnum', 'email', 'mode', 'add1', 'add2', 'city', 'region', 'zip', 'delivery','specints')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)