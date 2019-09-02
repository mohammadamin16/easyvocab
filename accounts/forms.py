from django import forms
from django.contrib.auth import get_user_model


class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=40)
    display_name = forms.CharField(max_length=140)
    display_name = forms.CharField(max_length=140)
    password = forms.CharField(widget=forms.PasswordInput())

    def save_user(self):
        get_user_model().objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['username'],
            self.cleaned_data['display_name'],
            self.cleaned_data['password']
        )



