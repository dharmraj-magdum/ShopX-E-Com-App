from django.urls import path
from .views import funtion_views as views
from .views.home import HomeView, filtered_list, specific_filter_list
from .views.profile import ProfileView
urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('product-detail/<int:pk>',
         views.product_Detail, name='product-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('filtered-list/<str:category>/<str:spec>/<int:amount>',
         specific_filter_list, name='specific-filter-list'),
    path('filtered-list/<str:category>',
         filtered_list, name='filtered-list'),
]
# //for ajax/ funtional not render
urlpatterns += [
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-gateway/', views.payment_gateway, name='payment-gateway'),
]
# //for ajax/ funtional not render
urlpatterns += [
    path('change-cart/', views.change_cart, name='change-cart'),
    path('remove-cart/', views.remove_cart, name='remove-cart'),
]
