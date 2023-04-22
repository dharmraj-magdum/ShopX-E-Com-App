from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserLoginForm, UserUpdateForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
# from ..shop.models import Customer, Product, Category, Cart, Order


class RegisterUser(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/registerForm.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('user-login')
        return render(request, 'users/registerForm.html', {'form': form})


# class LoginUser(View):
#    def post(self, request):
#         form = UserLoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('index')
#         else:
#             messages.error(request, 'username or password not correct')
#             return redirect('login')

#     else:
#         form = AuthenticationForm()
#     return render(request, 'todo/login.html', {'form': form})
