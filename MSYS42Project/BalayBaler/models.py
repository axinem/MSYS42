from django.db import models
from django.utils import timezone
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

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
