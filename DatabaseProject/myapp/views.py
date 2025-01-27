from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        stdata=studForm(request.POST)
        if stdata.is_valid():
            stdata.save()
            print("Your data has been saved!")
            msg="Your data has been saved!"
        else:
            print(stdata.errors)
            msg="Error!Something went wrong..."
    return render(request,'index.html',{'msg':msg})

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    msg=""
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        update=updateForm(request.POST,instance=stid)
        if update.is_valid():
            update.save()
            print("Your data has been updated!")
            msg="Your data has been updated!"
            return redirect('showdata')
        else:
            print(update.errors)
            msg="Error...Something went wrong!"
    return render(request,'updatedata.html',{'stid':stid,'msg':msg})