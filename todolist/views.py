from django.shortcuts import get_object_or_404, render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from todolist.models import Task
from todolist.forms import TaskForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'data_task': data_task,
        'user': request.user,
    }
    return render(request, "todolist.html", context)


@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todolist:show_todolist')
        
    context = {'form':form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.delete()
        return redirect('todolist:show_todolist')
        
    messages.error(request, 'Error! Tidak dapat menghapus task')
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def show_json(request):
    user = request.user
    data = Task.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Task.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)
        result = {
            'pk':todo.pk,
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'is_finished':todo.is_finished,
                'date':todo.date,
            }
        }
        return JsonResponse(result)    
    return HttpResponseBadRequest()

