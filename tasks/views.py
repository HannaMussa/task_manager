from django.shortcuts import render, redirect
from .models import Task  # show tasks
from .forms import TaskForm  # create form


def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # show task for that user
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'form': form
    })
