from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Cart, CartItem
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
  
def info_view(request):
    return render(request, 'info.html')
  
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
  
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    selected_size = request.POST.get('size')
    quantity = int(request.POST.get('quantity'))  

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = Cart() 

    cart_item, created = CartItem.objects.get_or_create(product=product, size=selected_size)

    if created: 
        cart.items.add(cart_item)
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity  
        cart_item.save()

    cart.save()

    if selected_size == '100g':
        if product.stock_100g >= quantity:  
            product.stock_100g -= quantity
        else:
            return redirect('out_of_stock_page')
    elif selected_size == '4L':
        if product.stock_4L >= quantity:
            product.stock_4L -= quantity
        else:
            return redirect('out_of_stock_page')
    elif selected_size == '6L':
        if product.stock_6L >= quantity:
            product.stock_6L -= quantity
        else:
            return redirect('out_of_stock_page')

    product.save()
    return redirect('cart')

def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
    else:
        items = []  

    total_price = sum(item.product.price_100g if item.size == '100g' else
                      item.product.price_4L if item.size == '4L' else
                      item.product.price_6L * item.quantity
                      for item in items)

    return render(request, 'cart.html', {'items': items, 'total_price': total_price})
  
def update_cart(request):
    if request.method == 'POST':
        for item_id, quantity in request.POST.items():
            if item_id.startswith('quantity_'):
                item_id = item_id.split('_')[1]
                try:
                    item = CartItem.objects.get(id=item_id)
                    quantity = int(quantity)
                    if quantity == 0:
                        item.delete()  
                        messages.info(request, f'{item.product.name} has been removed from your cart.')
                    else:
                        item.quantity = quantity
                        item.save()
                except CartItem.DoesNotExist:
                    pass
        if 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            try:
                item = CartItem.objects.get(id=item_id)
                product = get_object_or_404(Product, id=item_id)
                if item.size == '100g':
                    product.stock_100g += quantity
                item.delete()
                messages.success(request, f'{item.product.name} has been deleted from your cart.')
            except CartItem.DoesNotExist:
                pass

    return redirect('cart')
  
def product_list(request):
    products = Product.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)

    selected_category = request.GET.get('category', '')
    if selected_category:
        products = products.filter(category__name=selected_category)

    context = {
        'products': products,
    }
    return render(request, 'your_template.html', context)
  

def checkout(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phonenum = request.POST.get('phonenum')
        email = request.POST.get('email')
        
        delivery_type = request.POST.get('delivery_type')
        delivery_fee = 0
        
        error_messages = []

        if not fname:
            error_messages.append("First Name is required.")
        if not lname:
            error_messages.append("Last Name is required.")
        if not phonenum:
            error_messages.append("Phone Number is required.")
        if not email:
            error_messages.append("Email is required.")
        
        if delivery_type == 'delivery':
            add1 = request.POST.get('add1')
            add2 = request.POST.get('add2')
            city = request.POST.get('city')
            region = request.POST.get('region')
            zipc = request.POST.get('zipc')

            if not add1:
                error_messages.append("Address Line One is required.")
            if not city:
                error_messages.append("City is required.")
            if not region:
                error_messages.append("Region is required.")
            if not zipc:
                error_messages.append("ZIP Code is required.")

            if city in ['Manila']:
                delivery_fee = 250
            elif city in ['Mandaluyong', 'Marikina', 'Pasig', 'Quezon City', 'San Juan']:
                delivery_fee = 300
            elif city in ['Caloocan', 'Malabon', 'Navotas', 'Valenzuela']:
                delivery_fee = 350
            elif city in ['Las Piñas', 'Makati', 'Muntinlupa', 'Parañaque', 'Pasay', 'Pateros', 'Taguig']:
                delivery_fee = 100

        elif delivery_type == 'pickup':
            special_instructions = request.POST.get('special_instructions')
        
        if error_messages:
            for message in error_messages:
                messages.error(request, message)
            return render(request, 'checkout.html', {'delivery_fee': delivery_fee})

        messages.success(request, 'Your order has been successfully placed!')
        return redirect('thankyou.html')

    return render(request, 'checkout.html')


def process_order(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phonenum = request.POST.get('phonenum')
        email = request.POST.get('email')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        city = request.POST.get('city')
        region = request.POST.get('region')
        zipc = request.POST.get('zipc')

        messages.success(request, "Order placed successfully!")

        return redirect('thankyou')
    
    else:
        return redirect('checkout')

def thankyou(request):
    if 'fname' in request.session:
        del request.session['fname']
    if 'lname' in request.session:
        del request.session['lname']
    if 'phonenum' in request.session:
        del request.session['phonenum']
    if 'email' in request.session:
        del request.session['email']
    if 'add1' in request.session:
        del request.session['add1']
    if 'city' in request.session:
        del request.session['city']
    if 'region' in request.session:
        del request.session['region']
    if 'zipc' in request.session:
        del request.session['zipc']

    return render(request, 'thankyou.html')