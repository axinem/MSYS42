from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  
    

    price_100g = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_4L = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_6L = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
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
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name