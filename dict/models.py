from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=60)
    definition = models.TextField(default='')
    translation = models.CharField(max_length=100)
    example = models.TextField(default='')

    def __str__(self):
        return self.word

