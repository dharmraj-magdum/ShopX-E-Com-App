from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from .product import Product
from .customer import Customer
from .cart import Cart

STATUS = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateField(editable=False)
    status = models.CharField(
        choices=STATUS, max_length=30, default="Pending", blank=False)

    def save(self, *args, **kwargs):
        # ''' On save timestamps '''
        self.ordered_date = timezone.now()
        return super().save(*args, **kwargs)

    @property
    def get_subtotal(self):
        amount = (self.product.discounted_price*self.quantity)
        return amount

    @property
    def progress_bar(self):
        html = 'style=width:25%;background-color:var(--bs-orange);'
        # html = 'style=width:25%'
        if (self.status == "Accepted"):
            html = 'style=width:50%;background-color:var(--bs-yellow);'
        elif (self.status == "Packed"):
            html = 'style=width:75%;background-color:var(--bs-teal);'
        elif (self.status == "Delivered"):
            html = 'style=width:100%;background-color:var(--bs-success);'
        elif (self.status == "Cancel"):
            html = 'style=width:100%;background-color:var(--bs-red);'
        return str(html)

    def __str__(self):
        return f"{self.status} product-{self.product} quantity: {self.quantity}"
