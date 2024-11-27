from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


    
def minValue(value):
    if value < 0.00:
        raise ValidationError(
            ("%(value)s must be above 0."),
            params={"value": value},
        )

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  
    

    price_100g = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[minValue])
    price_4L = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[minValue])
    price_6L = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[minValue])
    
    stock_100g = models.PositiveIntegerField(default=0)
    stock_4L = models.PositiveIntegerField(default=0)
    stock_6L = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
      
class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.size})"

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    items = models.ManyToManyField(CartItem, blank=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
class Customer(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phnum = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=100)
    mode = models.CharField(max_length=10)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=10)
    zip = models.IntegerField(default=0)
    delivery = models.IntegerField(default=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name