from django.shortcuts import render

def task_list(request):
    # Your view logic here
    return render(request, 'tasks/index.html')