from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm



def index(request):
    all_task = Task.objects.all()
    return render(request, 'index.htm', {'all_task':all_task})

@login_required
def todolist(request):
    task_form = TaskForm()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save(commit=False).manage = request.user
            task_form.save()
            messages.success(request, ('task added successfully!')) 
    
    all_task = Task.objects.filter(manage = request.user)
    paginator = Paginator(all_task, 5)
    page = request.GET.get('pg')
    all_task = paginator.get_page(page)
    return render(request, 'todo.htm', {'all_task':all_task, 'task_form':task_form})

@login_required
def Edit_view(request, task_id):
    if request.method == 'POST':
        task_obj = Task.objects.get(pk=task_id)
        task_form = TaskForm(request.POST, instance=task_obj)
        if task_form.is_valid:
            task_form.save()
        return redirect('todo')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.htm', {'task_obj':task_obj})

@login_required
def delete_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.manage == request.user: 
        task.delete()
    else:
        messages.error(request, ('Page restricted, Not allowed!'))
    return redirect('todo')

@login_required
def completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ('Page restricted, Not allowed!'))
    return redirect('todo')

@login_required
def pending(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ('Page restricted, Not allowed!'))
    return redirect('todo')