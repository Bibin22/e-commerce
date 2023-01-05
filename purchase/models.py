from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.models import User


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('products.Products', models.CASCADE, null=True, blank=True)
    quantity = models.CharField(max_length=5, null=True, blank=True)
    amount = models.CharField(max_length=10, null=True, blank=True)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)