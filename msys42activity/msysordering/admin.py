from django.contrib import admin
from .models import Item, Order, ItemOrder

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount_paid', 'order_date', 'payment_type') 
    list_filter = ('payment_type',) 
    search_fields = ('id',) 

class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'order', 'quantity', 'line_total') 
    list_filter = ('order', 'item')  
    search_fields = ('id',)  

admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder, ItemOrderAdmin)
