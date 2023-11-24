from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.views import generic


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"


class MyLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return self.request.GET.get("next", reverse("todo-list"))
