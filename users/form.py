from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label="Enter password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label="Confirm password")
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control"}), label="Enter Email")

    class Meta:
        model = User
        widgets = {"username": forms.TextInput(
            attrs={"class": "form-control"})}
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autocomplete": "current-password", "autofocus": True, "class": "form-control"}), label="Enter Username")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"autocomplete": "current-password", "class": "form-control"}), strip=False, label="Enter password")


class UserPasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label="Enter your Old password")
    new_password1 = forms.CharField(
        label=_("Enter New Password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password",
                   "autofocus": True, "class": "form-control"}
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Enter Your Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={"autocomplete": "email", "class": "form-control"}),
    )


class UserPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("Enter New password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_image']
