from django.shortcuts import render, redirect
from django.utils import timezone
import pytz
from datetime import timedelta

from task.models import Task


def home(request):
    tz = pytz.timezone('Europe/Kyiv')

    days_from_now = timezone.now().astimezone(tz) + timedelta(days=1)
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    active_tasks = Task.objects.filter(completed=False).count()
    
    todey_task = Task.objects.filter(duedate__date=timezone.now().astimezone(tz).date(), completed=False).count()
    end_tasks = Task.objects.filter(duedate__date__lt=timezone.now().astimezone(tz).date(), completed=False).count()
    upcoming_tasks = Task.objects.filter(duedate__gte=days_from_now, completed=False).count()

    low_priority_tasks = Task.objects.filter(priority = 1).count()
    medium_priority_tasks = Task.objects.filter(priority = 2).count()
    high_priority_tasks = Task.objects.filter(priority = 3).count()
    
    data = {
        'total_tasks':total_tasks,
        'completed_tasks':completed_tasks,
        'active_tasks':active_tasks,
        'low_priority_tasks':low_priority_tasks,
        'medium_priority_tasks':medium_priority_tasks,
        'high_priority_tasks':high_priority_tasks,
        'todey_task':todey_task,
        'end_tasks':end_tasks,
        'upcoming_tasks':upcoming_tasks,
    }
    
    return render(request, 'main/home.html', data)
