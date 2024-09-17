from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    phonenum = models.CharField(null=False, blank=False, unique=True, max_length=20)
    email = models.EmailField((""), max_length=254)
    add1 = models.CharField(max_length=300)
    add2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    region = models.CharField(max_length=30)
    zipc = models.CharField(max_length=10)


class Size(models.Model):
    SIZE_CHOICES = [
        ('100g', '100g'),
        ('1L', '1L'),
        ('6L', '6L'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, unique=True)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    available_sizes = models.ManyToManyField(Size, through='ProductSizeStock')

    def __str__(self):
        return self.name


class ProductSizeStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock_level = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} - {self.size.size} (Stock: {self.stock_level}, Price: ₱{self.price})"



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


