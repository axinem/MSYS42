from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()

    objects = models.Manager()
    
    def getPrice(self):
       return self.item_price
    def getName(self):
       return self.item_name
    def __str__(self):
        return str(self.pk) + ": " + self.item_name
    
class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('gcash', 'GCash'),
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
    ]

    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    
    objects = models.Manager()

    def __str__(self):
        return f"Order {self.pk} - Total: {self.total_amount_paid} PHP"

class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    objects = models.Manager()

    def __str__(self):
        return f"Order {self.order.pk} - Item {self.item.name}: {self.quantity} pcs - Line Total: {self.line_total} PHP"

    def calculate_line_total(self):
        self.line_total = self.quantity * self.item.price
        return self.line_total