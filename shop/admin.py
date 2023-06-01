from django.contrib import admin
from .models.customer import Customer
from .models.product import Product
from .models.category import Category
from .models.cart import Cart
from .models.order import Order


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ["id", "user", "name", "address", "city",]


# //----#dependent---------------------

@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ["id", "title", "category", "discounted_price"]


@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity"]


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ["id", "status", "user", "customer",
                    "ordered_date", "product", "quantity"]
