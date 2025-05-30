from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    todos = {
        'todos': Todo.objects.all(),
        'title': 'Todo List',
        'description': 'A simple todo list application'
    }
    return render(request, 'home.html', todos)

def about(request):
    context = {'name': 'Hugo Loiola', 'age': '22'}
    return render(request, 'about.html', context)