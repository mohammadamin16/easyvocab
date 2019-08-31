from django import forms


class SearchboxForm(forms.Form):
    searchbox = forms.CharField()


