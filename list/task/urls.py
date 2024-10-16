from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_home, name='task_home'),
    path('create', views.task_create, name='task_create'),
    path('notification', views.notification, name='notification'),
    path('<int:pk>/delete', views.NewTaskDelete.as_view(), name = 'task-delete'),
    path('<int:pk>/update', views.TaskCompleted.as_view(), name='task_completed'),
]