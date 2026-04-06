from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.schedule_task, name='result'),
    path('tasks/', views.view_tasks, name='tasks'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]