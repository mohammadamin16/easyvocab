from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)