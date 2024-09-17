from django.contrib import admin
from .models import Product, Size, ProductSizeStock


class ProductSizeStockInline(admin.TabularInline):
    model = ProductSizeStock
    extra = 1
    fields = ['size', 'stock_level', 'price']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductSizeStockInline]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
