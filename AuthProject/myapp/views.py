from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login successfully!")
            msg="Login successfully!"
            return redirect('home')
        else:
            print("Error!Login faild....")
            msg="Error!Login faild...."
    return render(request,'index.html',{'msg':msg})

def signup(request):
    msg=""
    if request.method=='POST':
        newreq=signupForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Signup Successfully!")
            msg="Signup Successfully!"
            return redirect('/')
        else:
            print(newreq.errors)
            msg="Error!Something went wrong..."
    return render(request,'signup.html',{'msg':msg})

def home(request):
    return render(request,'home.html')