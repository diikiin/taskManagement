from django.contrib import admin

from .models import Task, Project, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    filter_horizontal = ('tags',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
