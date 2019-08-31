from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Word


def index(request):
    if request.method == 'POST':
        form = forms.SearchboxForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['searchbox']
            try:
                word = Word.objects.get(word=q)
            except Exception as e:
                form = forms.SearchboxForm()
                return render(request, 'dict/index.html', dict(form=form, error=True))
            translation = word.translation
            defi = word.definition
            example = word.example

            return render(request, 'dict/index.html',
                          dict(form=form, word=word, translation=translation,example=example, defi=defi ))

    form = forms.SearchboxForm()
    return render(request, 'dict/index.html', dict(form=form))
