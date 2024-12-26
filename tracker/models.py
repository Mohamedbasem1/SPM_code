from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ('backlog', 'Backlog'),
        ('doing', 'Doing'),
        ('review', 'Review'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='backlog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assign_to= models.TextField()

    def __str__(self):
        return self.title
class Project(models.Model):
   title = models.CharField(max_length=200)
   Capital = models.CharField(max_length=200)
   description = models.TextField()
def __str__(self):
    return self.title
