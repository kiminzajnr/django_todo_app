from django.urls import path

from .import views


app_name = "ToDo"
urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:task_id>", views.edit_task, name="edit_task"),
    path("delete/<int:task_id>", views.delete_task, name="delete_task"),
]