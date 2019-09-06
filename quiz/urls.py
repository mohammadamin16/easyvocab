from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.QuizList.as_view() , name='index'),
    path('result', views.QuizResult.as_view() , name='result'),
    path('<pk>', views.QuizView.as_view(), name='quiz-view'),
    path('correct', views.correct , name='correct'),
    path('wrong', views.wrong , name='wrong'),
]

