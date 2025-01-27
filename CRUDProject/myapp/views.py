from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        newreq=userForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Data inserted!")
        else:
            print(newreq.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        newreq=updateForm(request.POST,instance=stid)
        if newreq.is_valid():
            newreq.save()
            print("Data updated!")
            return redirect('showdata')
        else:
            print(newreq.errors)
    return render(request,'updatedata.html',{'stid':stid})


def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect('showdata')

    
