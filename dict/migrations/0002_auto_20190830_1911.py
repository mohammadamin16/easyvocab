# Generated by Django 2.2.4 on 2019-08-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='definition',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='word',
            name='example',
            field=models.TextField(default=''),
        ),
    ]
