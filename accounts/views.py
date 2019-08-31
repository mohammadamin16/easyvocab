from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class =  AuthenticationForm
    success_url = redirect('home')

    def form_valid(self, form):
        print("VALID")
        return super().form_valid(form)



