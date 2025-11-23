from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.utils import timezone


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = False
    task.save()
    return redirect("home")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        new_task_content = request.POST.get('task')
        task.task = new_task_content
        task.save()
        return redirect('home')

    context = {'task': task}
    return render(request, 'edit_task.html', context)
