# Generated by Django 2.2.4 on 2019-09-08 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'quizzes'},
        ),
    ]