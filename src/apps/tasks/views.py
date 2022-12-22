from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    context = {
        'title': 'Главная страница сайта', 
        'tasks': tasks
        }
    return render(request, 'tasks/index.html', context)

def about(request):
    return render(request, 'tasks/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
            
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'tasks/create.html', context)    