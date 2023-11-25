from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("create_todo/", views.create_todo, name="todo-create"),
    path(
        "toggle_todo_status/<int:todo_id>",
        views.toggle_todo_status,
        name="todo-toggle-status",
    ),
]
