from django.db import models
from django.utils import timezone
#from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    phonenum = models.CharField(null=False, blank=False, unique=True, max_length=20)
    email = models.EmailField((""), max_length=254)
    add1 = models.CharField(max_length=300)
    add2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    region = models.CharField(max_length=30)
    zipc = models.CharField(max_length=10)

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price

class Cart(models.Model):
    session_key = models.CharField(max_length=255, unique=True)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f"Cart {self.session_key}"

    @property
    def cart_total(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def cart_items_count(self):
        return sum(item.quantity for item in self.items.all())


