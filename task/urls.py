from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/done/', views.task_done, name='task_done'),
]
