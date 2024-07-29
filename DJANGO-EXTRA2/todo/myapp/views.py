from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    return render(request,"home.html")

def todo(request):

    todos= Todo.objects.filter(is_completed=False)
    todos2=Todo.objects.filter(is_completed=True)

    parameters={
        "name":"Muskan",
        "todos":todos,  
        "todos2":todos2 
    }

    return render(request,"todo.html",parameters)
#===============ADD TODO================================
def add_todo(request):

    if request.method == "POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at") 

        new_todo = Todo(
            task=user_task,
            created_at=user_created_at,
            is_completed=False
            )
        
        new_todo.save( )

        return redirect("todo")

    return render(request,"add_todo.html")
#========DELETE TODO====================================
def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("todo")
#==========UPDATE TODO==================================
def update_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)

    if request.method == "POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at")

        todo.task=user_task
        todo.created_at=user_created_at
        todo.save()
        return redirect("todo")
    
    parameters ={
        'todo':todo
    }

    return render(request,"update_todo.html",parameters)

#===================== COMPLETED TODO ==================
def mark_complete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_completed = True 
    todo.save()
    return redirect("todo")

