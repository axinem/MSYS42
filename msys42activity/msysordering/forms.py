from django import forms
from .models import Item, Order, ItemOrder

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['total_amount_paid', 'payment_type']

class ItemOrderForm(forms.ModelForm):
    class Meta:
        model = ItemOrder
        fields = ['item', 'quantity']