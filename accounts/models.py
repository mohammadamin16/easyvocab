from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.contrib.auth.models import User
from django.db import models


# this is my customized User Model

class UserManager(BaseUserManager):

    def create_user(self, email, username, display_name, password):
        if not email:
            raise ValueError("Users must have Email")
        if not display_name:
            display_name = username

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            display_name=display_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, username, display_name, password):
        user = self.create_user(
            email,
            username,
            display_name,
            password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    display_name = models.CharField(max_length=140)
    bio = models.CharField(max_length=140, blank=True, default="")
    avatar = models.ImageField(blank=)


