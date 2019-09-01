from django import forms


class TestForm(forms.Form):
    answer = forms.CharField(max_length=20)


