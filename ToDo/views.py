from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('ToDo:index')
    return render(request, "ToDo/index.html", {"tasks": tasks, "form": form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('ToDo:index')
