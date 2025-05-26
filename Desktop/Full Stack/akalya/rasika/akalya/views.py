from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def homepage(request):
    return render (request,'index.html')




def student_form (request):
    if request.method =='POST':
        name=request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        email=request.POST.get('email')
        student.objects.create(name=name,roll_no=roll_no,email=email)
        return redirect('student_form')
    

    students=student.objects.all()
    return render(request,'index.html',{'students':students})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
 
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
            return redirect('signup')
        
        user =User.objects.create_user(username=username,email=email,password=password)
        messages.success(request, "account created successfully")
        return redirect('login')
    
    return render(request,'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,  username= username,password =password, )
        if User:
            login(request, user)
            return redirect('student_form')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
        
    return render(request,'login.html')
        
def student_biodata(request):
    if request.method =='POST':
        dept=request.POST.get('dept')   
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        mobile_no=request.POST.get('mobile_no')
        stream=request.POST.get('stream')
        biodata.objects.create( dept=dept ,age=age , gender= gender ,mobile_no=mobile_no ,stream=stream )
        return redirect('student_biodata')
    

    biodatas=biodata.objects.all
    return render(request,'biodata.html',{'biodatas':biodatas})


def edit_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)

    if request.method == "POST":
        biodatas.title = request.POST.get("title")
        biodatas.description = request.POST.get("description")
        biodatas.credits = request.POST.get("credits")
        biodatas.save()
        return redirect("biodatas_ui")

    return render(request, "delete.html"), {
        "edit_biodata": biodatas,
        "courses": biodata.objects.all()
    }


def delete_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)
    biodatas.delete()
    return redirect("biodatas-ui")

