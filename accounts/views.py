from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.urls import reverse
from django.views.generic import FormView


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        print("VALID")
        return super().form_valid(form)
