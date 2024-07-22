from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_pass = request.POST.get('confirmpassword')
        if password == con_pass:
            user = User.objects.create_user(username=name,email=email,password=password)
            user.save()
        else:
            return HttpResponse('Password not match')
        return redirect('login')

    return render(request,'register.html')
    



def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = name,password = password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('read')
    return render(request,'login.html')



def read(request):
    return render(request,'read.html')

def forgot_pass(request):
    return render(request,'forgot-password.html')

def index(request):
    return render(request,'index.html')



