from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, FormView

from . import forms
from .models import Word


def index(request):
    if request.method == 'POST':
        form = forms.SearchboxForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['searchbox']
            try:
                word = Word.objects.get(word=q)
                if str(request.user) == 'AnonymousUser':pass
                else:
                    user = get_user_model().objects.get(username=request.user.username)
                    user.words.add(word)
            except Exception as e:
                # raise e
                form = forms.SearchboxForm()
                return render(request, 'dict/index.html', dict(form=form, error=True))
            translation = word.translation
            defi = word.definition
            example = word.example
            print('TEST')
            print(request.user)
            return render(request, 'dict/index.html',
                          dict(form=form, word=word, translation=translation,example=example, defi=defi ))

    form = forms.SearchboxForm()
    return render(request, 'dict/index.html', dict(form=form))


class AddWord(FormView):
    model = Word
    form_class = forms.AddWordForm
    template_name = 'dict/add_word.html'

    def form_valid(self, form):
        form.add_word()
        return super(AddWord, self).form_valid(form)

    def get_success_url(self):
        return reverse('dict:index')