from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('<int:project_id>/tasks/<int:task_id>/change-status/', views.change_status, name='change_status'),

    path('<int:project_id>/create/', views.create_task, name='create'),
    path('add_project/', views.add_project, name='add_project'),
    path('<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete'),
]