from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .category import Category
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=80)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return f"id- {self.id}  title- {self.title}"

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


    