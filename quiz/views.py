from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from quiz import forms
from quiz.models import Question, Quiz


class QuizList(ListView):
    model = Quiz
    context_object_name = 'quizzes'
    template_name = 'quiz/index.html'


class QuizView(DetailView):
    model = Quiz
    template_name = 'quiz/quiz_view.html'
    context_object_name = 'quiz'

    def post(self, request, *args, **kwargs):
        # self.request.session['pre'] = ''
        try:
            pre = self.request.session['pre']
        except Exception as e:
            pre = ''
        pre = pre.split(',')
        r = self.request.POST['ans']
        pre.append(r)
        response = ','.join(pre)
        request.session['pre'] = response

        if self.is_finished():
            return HttpResponseRedirect(reverse('quiz:result'))

        return self.get(request, *args, **kwargs)

    def is_finished (self):
        try:
            if int(self.request.POST['QO']) == self.get_object().questions.count():
                return True
            else:
                return False

        except Exception as e:
            pass

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['quiz_number'] = self.get_object().pk
        self.request.session['quiz_number'] = context['quiz_number']
        try:
            context['QO'] = int(self.request.POST['QO'])
        except Exception as e:
            context['QO'] = 0

        choices = self.get_object().questions.all()[context['QO']].choices.split(',')
        context['choice1'] = choices[0]
        context['choice2'] = choices[1]
        context['choice3'] = choices[2]
        context['choice4'] = choices[3]
        return context


class QuizResult(TemplateView):
    template_name = 'quiz/result.html'

    def process_quiz(self):
        answers = self.pre.split(',')
        quiz = Quiz.objects.get(pk=self.request.session['quiz_number'])
        points = 0
        counter = 0
        for question in quiz.questions.all():
            counter += 1
            print(question.answer, '==', answers[counter])
            print(answers)
            if question.answer == answers[counter]:
                points += question.difficulty
        self.add_point_to_user(points)
        return points

    def add_point_to_user(self, point):
        user = self.request.user
        user.point += point
        user.save()

    def get(self, request, *args, **kwargs):
        try:
            self.pre = self.request.session['pre']
        except Exception as e:
            return HttpResponseRedirect(reverse('quiz:index'))
        del self.request.session['pre']
        return super(QuizResult, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuizResult, self).get_context_data(**kwargs)
        context['pre'] = self.pre
        context['points'] = self.process_quiz()
        return context


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