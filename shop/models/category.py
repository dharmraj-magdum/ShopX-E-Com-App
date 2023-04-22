from django.db import models
from django.shortcuts import get_object_or_404


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_ID_category(n):
        category = Category.objects.filter(name=n)
        if len(category) >= 1:
            return category[0].id
        return 1

    @staticmethod
    def get_all_categories_asList():
        list = []
        for category in Category.objects.all():
            list.append(category.name)
        return list

    def __str__(self):
        return self.name
