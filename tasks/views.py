from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task  # show tasks
from .forms import TaskForm  # create form


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # show task for that user
    form = TaskForm(request.POST or None)

    if request.method == 'POST' and 'task_id' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.completed = not task.completed
        task.save()

     # if form is valid, create a new task
    elif request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task-list')

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'form': form,
    })

# edit task


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')

    else:
        form = TaskForm(instance=task)  # Populate form with current task data

    return render(request, 'tasks/edit.html', {'form': form, })

# delete task


@login_required
def task_delete(request,  pk):
    task = get_object_or_404(Task, pk=pk,  user=request.user)
    task.delete()
    return redirect('task-list')
