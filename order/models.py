from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class OrderStatus(models.TextChoices):
    PROCESSING = 'processing', 'Processing'
    SHIPPED = 'shipped', 'Shipped'
    DELIVERED = 'delivered', 'Delivered'

class PaymentStatus(models.TextChoices):
    PAID = 'paid', 'Paid'
    UNPAID = 'unpaid', 'Unpaid'

class PaymentMode(models.TextChoices):
    COD = 'cod', 'Cash on Delivery'
    CARD = 'card', 'Card'

class Order(models.Model):
    order_status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.PROCESSING,
    )
    payment_status = models.CharField(
        max_length=6,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
    )
    payment_mode = models.CharField(
        max_length=4,
        choices=PaymentMode.choices,
        default=PaymentMode.COD,
    )
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - Status: {self.get_order_status_display()}, Payment: {self.get_payment_status_display()}, Mode: {self.get_payment_mode_display()}"
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id} - Product: {self.name}, Quantity: {self.quantity}, Price: {self.price}"
