from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["todo_task"]
        widgets = {
            'todo_task': forms.TextInput(attrs={'class': 'input is-primary', 'placeholder': 'Enter Todo'}),
        }