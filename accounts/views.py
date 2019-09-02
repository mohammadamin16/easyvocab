from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth import get_user_model

from accounts.forms import SignUpForm


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


class SignUp(FormView):
    form_class = SignUpForm
    fields = ['email', 'username', 'password', 'display_name']
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save_user()
        return super(SignUp, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:login')

