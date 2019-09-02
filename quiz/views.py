import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import log
from django.views.generic import DetailView, ListView

from quiz import forms
from quiz.models import Question, Quiz


class QuizList(ListView):
    model = Quiz
    context_object_name = 'quizzes'
    template_name = 'quiz/index.html'


def test(request):
    if request.method == 'POST':
        form = forms.TestForm(request.POST)
        if form.is_valid():
            qpk = request.POST.get('q')
            q = Question.objects.get(pk=qpk)
            print(q.answer)
            if form.cleaned_data['answer'] == q.answer:
                request.user.point += 1
                request.user.save()
                return HttpResponseRedirect(reverse('quiz:correct'))
            else:
                return HttpResponseRedirect(reverse('quiz:wrong'))

    question = Question.objects.order_by('?').first()
    form = forms.TestForm()
    return render(request, 'quiz/test.html', dict(form=form, question=question))


def correct(request):
    return render(request, 'quiz/correct.html')


def wrong(request):
    return render(request, 'quiz/wrong.html')