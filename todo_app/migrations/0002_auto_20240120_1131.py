# Generated by Django 3.0.3 on 2024-01-20 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
    ]