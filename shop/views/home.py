from django.shortcuts import render, redirect
from django.views import View
from ..models import Customer, Product, Category, Cart, Order


class HomeView(View):
    def get(self, request):
        topwears = Product.objects.filter(
            category=Category.get_ID_category("Top Wear"))
        bottomwears = Product.objects.filter(
            category=Category.get_ID_category("Bottom Wear"))
        mobiles = Product.objects.filter(
            category=Category.get_ID_category("Mobile"))
        context = {
            "topwears": topwears,
            "bottomwears": bottomwears,
            "mobiles": mobiles,
            "shop": "DK MART",
        }
        return render(request, "shop/home.html", context)


CATEGORY_LIST = Category.get_all_categories_asList()


def filtered_list(request, category):
    if (category in CATEGORY_LIST):
        product_list = Product.objects.filter(
            category=Category.get_ID_category(category))
        all = "active"
        context = {
            "all": all,
            "category": category,
            "product_list": product_list,
        }
        return render(request, 'shop/filtered_list.html', context)
    return redirect("home-page")


def specific_filter_list(request, category, spec, amount):
    if (category in CATEGORY_LIST):
        list = Product.objects.filter(
            category=Category.get_ID_category(category))
        if spec:
            above = ""
            below = ""
            if (spec == "below"):
                list = list.filter(discounted_price__lt=amount)
                below = "active"
            elif (spec == "above"):
                list = list.filter(discounted_price__gt=amount)
                above = "active"
        context = {
            "category": category,
            "above": above,
            "below": below,
            "product_list": list,
        }
        return render(request, 'shop/filtered_list.html', context)
    return redirect("home-page")
