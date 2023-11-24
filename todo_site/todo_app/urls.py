from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("create_todo/", views.create_todo, name="todo-create"),
]
