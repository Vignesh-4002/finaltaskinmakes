from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'index.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,'User not found')
            return redirect('userlogin')

    return render(request,'login.html')

def userlogout(request):
    auth.logout(request)
    return redirect('home')

def registeruser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        conpassword=request.POST['conpassword']

        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('userlogin')

        else:
            print("Password not matching")
            return redirect('registeruser')
    return render(request,'register.html')

def form(request):
    return render(request,'forms.html')