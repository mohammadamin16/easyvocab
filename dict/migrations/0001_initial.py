# Generated by Django 2.2.4 on 2019-08-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=60)),
                ('translation', models.CharField(max_length=100)),
            ],
        ),
    ]
