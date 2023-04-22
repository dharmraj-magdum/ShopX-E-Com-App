from django.urls import path
from .form import UserLoginForm, UserPasswordUpdateForm, UserPasswordResetForm, UserPasswordSetForm
from .views import RegisterUser
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="user-register"),
]

urlpatterns += [
    path('register/', RegisterUser.as_view(), name="user-register"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html", authentication_form=UserLoginForm),
         name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='user-login'),
         name="user-logout"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="users/password_change.html", form_class=UserPasswordUpdateForm, success_url="/users/password-change-done/"),
         name="user-password-change"),
    path("password-change-done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="users/password_change_done.html"), name="user-password-change-done"),
    path("password-reset/", auth_views.PasswordResetView.as_view(form_class=UserPasswordResetForm,
         template_name="users/password_reset.html"), name="user-password-reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
         template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(form_class=UserPasswordSetForm,
         template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
         template_name="users/password_reset_complete.html"), name="password_reset_complete")
]
