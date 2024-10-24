# Generated by Django 5.1 on 2024-10-22 06:20

from django.db import migrations


def add_initial_tasks(apps, schema_editor):
    Task = apps.get_model('task', 'Task')

    tasks = [
        {"title": "Create Django Application", "description": "Setting up Django project."},
        {"title": "Create Django Models", "description": "Migrate models to database."},
        {"title": "Start Task Management Project", "description": "Plan and start working on the project."},
    ]

    for task in tasks:
        Task.objects.create(**task)


class Migration(migrations.Migration):
    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_tasks)
    ]
