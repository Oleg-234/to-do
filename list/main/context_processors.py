from task.models import Task
from django.utils import timezone
import pytz


def main_context(request):
    tz = pytz.timezone('Europe/Kyiv')
    tasks = Task.objects.all()
    todey_task = Task.objects.filter(duedate__date=timezone.now().astimezone(tz).date(), completed=False).count()

    
    data = {
        'tasks':tasks,
        'todey_task':todey_task,
    }
    
    return data