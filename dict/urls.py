from django.urls import path
from . import views

app_name = 'dict'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_word', views.AddWord.as_view(), name='add-word'),
]
