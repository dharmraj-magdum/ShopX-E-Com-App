from django.shortcuts import HttpResponse, render, redirect
from django.views import View
from ..models import Customer, Product, Category, Cart, Order
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def product_Detail(request, pk):
    product = Product.objects.get(pk=pk)
    # // check is it in car t or not
    context = {}
    if (request.user.is_authenticated):
        in_cart = is_item_in_cart(request.user, product)
        if (in_cart):
            context = {"is_in_cart": True, "product": product}
        else:
            context = {"is_in_cart": False, "product": product}
    else:
        context = {"is_in_cart": False, "product": product}
    return render(request, 'shop/productdetail.html', context)


def is_item_in_cart(user, product):
    carts = Cart.objects.filter(user=user)
    in_cart = carts.filter(product=product).exists()
    return in_cart

# ///////////////////////protected routes/////////////////////////
# /////  related to cart   ///


@login_required
def add_to_cart(request):
    product_id = request.GET.get('product_id')
    # print("====================")
    # print(product_id)
    product = Product.objects.get(pk=product_id)
    in_cart = is_item_in_cart(request.user, product)
    if in_cart:
        return product_Detail(request, product_id)
    cart = Cart(user=request.user, product=product, quantity=1)
    cart.save()
    return product_Detail(request, product_id)


shiping_amount = 60


def makeSum(carts):
    amount = 0
    for cart in carts:
        amount += (cart.product.discounted_price*cart.quantity)
    return amount


@login_required
def show_cart(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    total = 0
    amount = 0
    if len(carts) <= 0:
        context = {"no_items": True, "carts": carts,
                   "amount": amount, "total": total}
    else:
        amount = makeSum(carts)
        total += amount+shiping_amount
        context = {"no_items": False, "carts": carts,
                   "amount": amount, "total": total}
    return render(request, 'shop/cart.html', context)

# -------modifications to cart-items in cart


@login_required
def change_cart(request):
    # print("got req")
    if not request.method == "GET":
        return HttpResponse("got post send GET Request")
    cur_user = request.user
    carts = Cart.objects.filter(user=cur_user)
    total = 0
    amount = 0
    product_id = request.GET.get("product_id")
    act = request.GET.get("act")
    # print(product_id)
    cur_cart = carts.get(product=product_id)
    if (act == 'add'):
        cur_cart.quantity += 1
    else:
        if (cur_cart.quantity > 1):
            cur_cart.quantity -= 1
    cur_cart.save()
   # //now recalc all amounts from cart
    amount = makeSum(carts)
    total += amount+shiping_amount
    context = {"quantity": cur_cart.quantity,
               "amount": amount, "total": total}
    return JsonResponse(context)


@login_required
def remove_cart(request):
    if not request.method == "GET":
        return HttpResponse("got post send GET Request")
    cur_user = request.user
    carts = Cart.objects.filter(user=cur_user)
    total = 0
    amount = 0
    product_id = request.GET.get("product_id")
    # print(carts)
    cur_cart = carts.get(product=product_id)
    cur_cart.delete()
    amount = makeSum(carts)
    total += amount+shiping_amount
    context = {"amount": amount, "total": total}
    return JsonResponse(context)

# ////////////////////////////////////////

# ///// checkout, orders related   ////


@login_required
def address(request):
    customerProflies = Customer.objects.filter(user=request.user)
    context = {"customerProflies": customerProflies}
    return render(request, 'shop/address.html', context)


@login_required
def checkout(request):
    cur_user = request.user
    carts = Cart.objects.filter(user=cur_user)
    # //one user van have multiple customer profiles
    customerProflies = Customer.objects.filter(user=cur_user)
    amount = makeSum(carts)
    total = 60+amount
    if len(customerProflies) <= 0:
        context = {"no_address": True, "carts": carts,
                   "amount": amount, "total": total}
    else:
        context = {"total": total, "amount": amount,  "carts": carts,
                   "customerProflies": customerProflies}
    return render(request, 'shop/checkout.html', context)


@login_required
def payment_gateway(request):
    # print("-----------------payment gateway")
    cur_user = request.user
    customer_id = request.GET.get("customer_id")
    cur_customer = Customer.objects.get(id=customer_id)
    carts = Cart.objects.filter(user=cur_user)
    # //now make an order
    # (in our model structure orders as seperate products are ordered)
    # //each cart meaning one order
    for cart in carts:
        order = Order(user=cur_user, customer=cur_customer,
                      product=cart.product, quantity=cart.quantity)
        order.save()
        cart.delete()
    # //after making order we empty users cart
    return redirect("orders")


@login_required
def orders(request):
    cur_user = request.user
    orders = Order.objects.filter(
        user=cur_user).order_by("-ordered_date")
    context = {"orders": orders}
    return render(request, 'shop/orders.html', context)


@login_required
def buy_now(request):
    # //here we just call add to cart
    product_id = request.GET.get('product_id')
    product = Product.objects.get(pk=product_id)
    in_cart = is_item_in_cart(request.user, product)
    if in_cart:
        return redirect("show-cart")
    cart = Cart(user=request.user, product=product, quantity=1)
    cart.save()
    # then go to cart
    return redirect("show-cart")
