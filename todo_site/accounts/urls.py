from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path(
        "login/", views.MyLoginView.as_view(), name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("register/", views.RegisterView.as_view(), name="register"),
]
