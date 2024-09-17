from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer

# Create your views here.

def base(request):
    return render(request, 'infotemp.html')

def checkout(request):
    if (request.method == "POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phonenum = request.POST.get('phonenum')
        email = request.POST.get('email')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        city = request.POST.get('city')
        region = request.POST.get('region')
        zipc = request.POST.get('zipc')

        Customer.objects.create(fname=fname, lname=lname, phonenum=phonenum, email=email, add1=add1, add2=add2, city=city, region=region, zipc=zipc)
        return redirect(thankyou)
    return render(request, 'checkout.html')

def thankyou(request):
    num = len(Customer.objects.all())
    customer = Customer.objects.order_by('id')[num-1]

    return render(request, 'thankyou.html', {'Customer': customer})

def dashboard(request):
    customer = Customer.objects.all()

    return render(request, 'dashboard.html', {'Customer': customer})