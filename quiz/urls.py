from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.QuizList.as_view() , name='index'),
    path('test', views.test , name='test'),
    path('correct', views.correct , name='correct'),
    path('wrong', views.wrong , name='wrong'),
]

