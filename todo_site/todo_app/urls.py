from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("todo/create/", views.create_or_update_todo, name="todo-create"),
    path("todo/<int:todo_id>/update/", views.create_or_update_todo, name="todo-update"),
    path(
        "toggle_todo_status/<int:todo_id>",
        views.toggle_todo_status,
        name="todo-toggle-status",
    ),
    path("get_cities/", views.get_cities, name="todo-get-cities"),
    path(
        "get_city_temperature/",
        views.get_city_temperature,
        name="todo-get-city-temperature",
    ),
]
