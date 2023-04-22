from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATES = (
    ("Rajasthan", "Rajasthan"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Gujarat", "Gujarat"),
    ("Kerala", "Kerala"),
    ("Nagaland", "Nagaland"),
    ("Punjab", "Punjab"),
    ("Haryana", "Haryana"),
    ("Uttarakhnd", "Uttarakhnd"),
    ("West Bengal", "West Bengal"),
    ("Assam", "Assam"),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    state = models.CharField(
        choices=STATES, max_length=50, default="Maharashtra", blank=False)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} name- {self.name}"
