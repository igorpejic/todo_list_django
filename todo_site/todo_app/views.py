from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    active_todos = todos.filter(is_done=False)
    done_todos = todos.filter(is_done=True)
    return render(
        request,
        "todo_app/todo_list.html",
        {"active_todos": active_todos, "done_todos": done_todos},
    )


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


@login_required
def toggle_todo_status(request, todo_id):
    todo = Todo.objects.filter(user=request.user, id=todo_id).first()
    if not todo:
        return HttpResponse(status=400)
    todo.is_done = not todo.is_done
    todo.save()
    return HttpResponse(status=200)
