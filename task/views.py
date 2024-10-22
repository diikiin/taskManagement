from django.shortcuts import render, get_object_or_404, redirect

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task/task_list.html', context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'task/task_detail.html', context)


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task/create_task.html')


def task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = True
    task.save()
    return redirect('task_list')
