from django import forms
from .models import Task
from .models import Project
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','assign_to', 'description', 'status', 'project')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'project': forms.TextInput(attrs={'class': 'form-title'}),
            'description': forms.Textarea(attrs={'class': 'form-desc'}),
            'status': forms.Select(attrs={'class': 'form-status'}),
            'assign_to': forms.TextInput(attrs={'class': 'form-title'})
        }
 
class ProjectForm(forms.ModelForm):
 class Meta:
    model = Project
    fields = ('title','Capital', 'description')
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-title'}),
        'description': forms.Textarea(attrs={'class': 'form-desc'}),
        'capital': forms.Textarea(attrs={'class': 'form-desc'}),
    }

