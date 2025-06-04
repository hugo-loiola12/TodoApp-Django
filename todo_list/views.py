from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {'name': 'Hugo Loiola', 'age': '22'}
    return render(request, 'about.html', context)