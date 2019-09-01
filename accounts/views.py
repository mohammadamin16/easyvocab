from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


class Login(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        return reverse('home')

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        return super().form_valid(form)


class Logout(LogoutView):
    def get_next_page(self):
        return reverse('home')


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return reverse('accounts:login')