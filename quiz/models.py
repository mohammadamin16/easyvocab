from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.title[:20]





