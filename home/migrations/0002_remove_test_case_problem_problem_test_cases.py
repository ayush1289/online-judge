# Generated by Django 4.1.10 on 2023-07-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_case',
            name='problem',
        ),
        migrations.AddField(
            model_name='problem',
            name='test_cases',
            field=models.ManyToManyField(to='home.test_case'),
        ),
    ]