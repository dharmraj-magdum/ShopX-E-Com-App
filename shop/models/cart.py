from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .product import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def get_subtotal(self):
        amount = (self.product.discounted_price*self.quantity)
        return amount

    def __str__(self):
        return f"{self.product.title} quantitiy-{self.quantity}"
