from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from ..models import Customer, Product, Category, Cart, Order
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "address", "city", "state"]
        myform = forms.TextInput(attrs={"class": "form-control"})
        widgets = {
            "name": myform,
            "address": myform,
            "city": myform,
            "state": forms.Select(attrs={"class": "form-control"}),
        }


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileForm()
        context = {
            "form": form,
        }
        return render(request, "shop/profile.html", context)

    def post(self, request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            newCustomer = Customer(**data, user=request.user)
            newCustomer.save()
            messages.success(
                request, f'Your profile has been created successfully!')
            return redirect('profile')
        else:
            pass
        context = {
            "form": form,
            "active": "active"
        }
        return render(request, "shop/profile.html", context)
