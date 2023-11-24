from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TodoForm


@login_required
def todo_list(request):
    return render(request, "todo_app/todo_list.html")


@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todo-list")
    else:
        form = TodoForm()

    return render(request, "todo_app/create_todo.html", {"form": form})
