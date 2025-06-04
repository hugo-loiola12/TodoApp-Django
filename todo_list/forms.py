from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    model = Todo
    fields = ['title', 'isCompleted']