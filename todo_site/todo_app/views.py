from django.shortcuts import render
from .forms import TodoForm


def todo_list(request):
    return render(request, "todo_app/todo_list.html")


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo_app/create_todo.html", {"form": form})
