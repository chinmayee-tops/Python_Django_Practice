from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session['cuser']=unm
            return redirect('home')
        else:
            print("Error...Login faild!")
            msg="Error...Login faild!"
    return render(request,'index.html',{'msg':msg})

def signup(request):
    if request.method=='POST':
        newreq=signupForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newreq.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('cuser')
    return render(request,'home.html',{'user':user})

def userlogut(request):
    logout(request)
    return redirect('/')
