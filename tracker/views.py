from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from .models import Project
from .forms import ProjectForm
def projects_list(request):
 return render(request, 'projects_list.html', {'projects': Project.objects.all()})
def task_list(request,project_id):
    tasks = {
        'backlog': Task.objects.filter(status='backlog', project=project_id),
        'doing': Task.objects.filter(status='doing', project=project_id),
        'review': Task.objects.filter(status='review', project=project_id),
        'done': Task.objects.filter(status='done', project=project_id),
    }
    task_counts = {status: queryset.count() for status, queryset in tasks.items()}
    return render(request, 'task_list.html', {'tasks': tasks, 'task_counts': task_counts,'project_id':project_id})


def change_status(request, project_id, task_id):
   task = get_object_or_404(Task, pk=task_id)

   if request.method == 'POST':
     new_status = request.POST.get('status')
     task.status = new_status
     task.save()
     return redirect('tracker:task_list', project_id=project_id)


def create_task(request, project_id):
    if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
        task = form.save(commit=False)
        task.project_id = project_id  # Associate the task with the project
        task.save()
        return redirect('tracker:task_list', project_id=project_id)
    else:
       form = TaskForm()
    return render(request, 'create_task.html', {'form': form, 'project_id': project_id})

def add_project(request):
 if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('tracker:projects_list')
 else:
    form = ProjectForm()
 return render(request, 'add_project.html', {'form': form})

def delete_task(request, task_id, project_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tracker:task_list', project_id=project_id)
