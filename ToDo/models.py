from django.db import models

class Task(models.Model):
    todo_task = models.CharField(max_length=5000)

    def __str__(self):
        return self.todo_task

