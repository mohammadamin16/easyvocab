from django.contrib import admin

from quiz.models import Question, Quiz

admin.site.register(Question)
admin.site.register(Quiz)