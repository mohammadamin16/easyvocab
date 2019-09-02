from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=300)
    choices = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.title[:20]


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.title[:20]

    @property
    def get_points(self):
        points = 0
        for q in self.questions.all():
            points += q.difficulty
        return points

    @property
    def get_number_of_questions(self):
        total = 0
        for q in self.questions.all():
            total += 1
        return total

