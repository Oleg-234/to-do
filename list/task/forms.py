from .models import Task
from django.utils import timezone
import pytz
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'duedate', 'priority', 'completed']
        tz = pytz.timezone('Europe/Kyiv')

        
        LOW = 1
        MEDIUM = 2
        HIGH = 3

        PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        ]
        
        widgets = {
            "title":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва',
            }),
            "description":Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опис',
            }),
            "duedate":DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'value': timezone.now().astimezone(tz).replace(hour=12, minute=0).strftime('%Y-%m-%dT%H:%M'),
            }),
            "priority": Select(attrs={
                'class': 'form-control',
            }, choices=PRIORITY_CHOICES),
        }