from django.db import models
from django.utils import timezone

class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    title = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')
    duedate = models.DateTimeField('Дата виконання')
    priority = models.PositiveSmallIntegerField('Пріоритет', choices=PRIORITY_CHOICES, default=MEDIUM)
    completed = models.BooleanField('Завершено', default=False)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
