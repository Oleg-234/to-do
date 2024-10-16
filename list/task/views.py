from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone
import pytz
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView


def task_create(request):
    task = Task.objects.order_by('-duedate')[:5]
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_home')
        else:
            error = 'Форму була невірною'
    
    form = TaskForm()
    
    data = {
        'error':error,
        'form':form,
        'task':task,
    }
    
    return render(request, 'task/create.html', data)

def task_home(request):
    task = Task.objects.order_by('-duedate')

    return render(request, 'task/task_home.html', {'task':task})

def notification(request):
    tz = pytz.timezone('Europe/Kyiv')
    current_date = timezone.now().astimezone(tz).date()
    task = Task.objects.all()
    task_todey = Task.objects.filter(duedate__date = current_date)
    
    data = {
        'task':task,
        'task_todey':task_todey, 
    }
    
    return render(request, 'task/notification.html', data)

class NewTaskDelete(DeleteView):
    model = Task
    success_url = '/task/'
    template_name = 'task/task-delete.html'
    
class TaskCompleted(UpdateView):
    model = Task
    success_url = '/task/'
    fields = ["completed"]
    template_name = 'task/task_completed.html'

