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


# удаление данных из бд
def delete(request, id):
    try:
        person = Task.objects.get(id=id)
        person.delete()
        return redirect('all_tasks')
    except Task.DoesNotExist:
        return redirect('error_404')


def error_404(request):
    return render(request, 'main/error_404.html')