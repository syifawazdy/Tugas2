import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from todolist.form import NewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

@login_required(login_url='/todolist/login/')
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist_ajax')           
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_todo(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            task = Task(
                user=request.user,
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
            )
            task.save()
            return redirect("todolist:show_todolist")

    form = NewForm()
    context = {"form": form}
    return render(request, "create_task.html", context)

def status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist_ajax'))

def delete(request, id):
    delete = Task.objects.get(pk=id)
    delete.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist_ajax'))

def show_todolist_ajax(request):
    data = Task.objects.filter(user=request.user).all()
    context = {
        'todo_list': data,
    } 
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task(
            date=str(datetime.date.today()),
            title=title, 
            description=description,
            user=request.user,
        )
        new_task.save()
    redirect('todolist:show_todolist_ajax')
    return HttpResponse('')
    

