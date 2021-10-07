
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    page = request.GET.get('page')
    id = request.GET.get('id')
    data = ""
    if page == 'dlt':
        delt = add_new_student.objects.filter(id = id)
        delt.delete()
    elif page == 'edit':
        data = add_new_student.objects.filter(id = id)
    value = add_new_student.objects.all().order_by('-id')
    return render(request,'index.html',context={'value':value,'data':data})

def add_student(request):
    value = add_new_student.objects.all().order_by('-id')
    if request.method == 'POST':
        name = request.POST.get('s_name')
        email = request.POST.get('s_email')
        password = request.POST.get('s_password')
        res = add_new_student(name = name, email = email, password = password)
        res.save()
    return render(request,'index.html',context={'value':value})

def update_student(request):
    if request.method == 'POST':
        id = request.POST.get('s_id')
        data = add_new_student.objects.get(id = id)
        data.name = request.POST.get('s_name')
        data.email = request.POST.get('s_email')
        data.password = request.POST.get('s_password')
        data.save()
    value = add_new_student.objects.all().order_by('-id')
    return render(request,'index.html',context={'value':value})