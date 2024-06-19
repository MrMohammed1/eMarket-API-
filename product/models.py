from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('computers', 'Computers'),
        ('kids', 'Kids'),
        ('food', 'Food'),
        ('home', 'Home'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="computers", blank=False)
    ratings = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
