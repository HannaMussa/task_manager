from django.shortcuts import render, redirect
from .models import Task  # show tasks
from .forms import TaskForm  # create form


def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # show task for that user
    form = TaskForm()
    
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
    })
    


def task_delete(request):
    Task.objects.get.delete()
    return redirect('task-list'