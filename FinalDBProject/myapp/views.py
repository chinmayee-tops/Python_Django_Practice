from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        newreq=studFomr(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Data has been saved!")
        else:
            print(newreq.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        newreq=studFomr(request.POST,instance=stid)
        if newreq.is_valid():
            newreq.save()
            print("Data has been updated!")
            return redirect('showdata')
        else:
            print(newreq.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')
