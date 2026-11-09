from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *





def home_page(request):
    context = { 
        'name': 'Abdullo',
        'age': 20,
        }
    return render(request, 'index.html', context)






def get_products(request):
    tasks = Tesks.objects.all()
    return render(request, 'show_task.html', {"tasks": tasks})


def add_tasks(request):
    if request.method == "POST":
        Tesks.objects.create(
            title = request.POST["title"],
            caption = request.POST["caption"],
            due_date = request.POST["due_date"]
        )
        return redirect('show_tasks')
    
    return render(request, "index.html")



def get_task_id(request, id):
    task = Tesks.objects.get(pk = id)
    return render(request, 'id.html', {"task": task})





def get_task_id_id(request, id):
    task = Tesks.objects.get(pk=id)

    if request.method == "POST":
        task.delete()
        return render(request, "delete.html")

    return render(request, "id.html", {"task": task})