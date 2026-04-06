from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Task

def home(request):
    return render(request, 'tracker/home.html')


def schedule_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        time = request.POST.get('time')
        frequency = request.POST.get('frequency')

        if not task or not time or not frequency:
            return render(request, 'home.html', {
                'error': 'All fields are required.'
            })

        Task.objects.create(
            name=task,
            time=time,
            frequency=frequency
        )

        return render(request, 'tracker/result.html', {
            'task': task,
            'time': time,
            'frequency': frequency
        })

    return redirect('home')


def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tracker/tasks.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')