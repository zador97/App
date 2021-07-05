from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-title')
    return render(request, 'main/index.html', {'title': 'Home page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'No valid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def all_tasks(request):
    context = {
        'title': 'Tasks list',
        'tasks': Task.objects.order_by('title')
    }

    return render(request, 'main/all_tasks.html', context)
