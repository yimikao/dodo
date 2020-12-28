from django.shortcuts import render, redirect

from .models import Tasks
from .forms import AddTaskForm

def index(request):

    tasks = Tasks.objects.all()
    form = AddTaskForm()

    context = {
        'tasks' : tasks,
        'form' : form,
    }

    return render(request, 'todo/index.html', context)


def addTask(request):
    
