from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Order, ItemOrder
from .forms import ItemForm, OrderForm, ItemOrderForm

def msysordering(request):
    return render(request, 'openpos.html')

def openpos_view(request):
    items = Item.objects.all()
    return render(request, 'openpos.html', {'items': items})

def item_list_view(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def configure_items(request):
    items = Item.objects.all()
    return render(request, 'configure.html', {'items': items})

def save_item(request):
    if request.method == 'POST':
        name = request.POST['item_name']
        price = request.POST['item_price']
        quantity = request.POST['item_quantity']
        item = Item(name=name, price=price, quantity=quantity)
        item.save()
    return redirect('configure_items')

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')  
    return render(request, 'delete_item_confirm.html', {'item': item})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  
            return redirect('add_items_to_order', order_id=order.id) 
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

def add_items_to_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = ItemOrderForm(request.POST)
        if form.is_valid():
            item_order = form.save(commit=False)
            item_order.order = order  
            item_order.line_total = item_order.calculate_line_total()  
            item_order.save()
            return redirect('view_order', order_id=order.id)  
    else:
        form = ItemOrderForm()
    return render(request, 'add_items_to_order.html', {'form': form, 'order': order})

def view_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    item_orders = ItemOrder.objects.filter(order=order)
    return render(request, 'view_order.html', {'order': order, 'item_orders': item_orders})

def delete_item_from_order(request, order_id, item_order_id):
    item_order = get_object_or_404(ItemOrder, id=item_order_id)
    if request.method == 'POST':
        item_order.delete()
        return redirect('view_order', order_id=order_id)
    return render(request, 'delete_item_order_confirm.html', {'item_order': item_order})