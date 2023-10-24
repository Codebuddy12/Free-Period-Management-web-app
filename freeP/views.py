from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Details
from .models import Days
from .models import Period
from django.contrib import messages
from .forms import Messages
from .forms import AddPeriod
from django.views import View
from django.contrib.auth.models import User,auth
from django.utils import timezone
# Create your views here.

def home(request):
    dest1=Details.objects.all()
    return render(request,'home.html',{'dest1':dest1})



def addFreePeriod(request):
    day=Days.objects.all()
    user=Period.objects.all()
    return render(request,'takePeriod.html',{'user':user,'day':day})

def addFreePeriodH(request):
    per=Period.objects.all()
    return render(request,'takefreePeriod2.html',{'per':per})

def addFree(request,pk):
    m=Period.objects.get(id=pk)
    n=Details.objects.get(Name=request.user)
    n.Reserve_Points=n.Reserve_Points+1
    n.save()
    form=AddPeriod(instance=m)
    if request.method=='POST':
        form=AddPeriod(request.POST,instance=m)
        if form.is_valid():
            form.save()
            return redirect('Details')
    context={'form':form}
    return render(request,'Takefree.html',context)

def addP(request,pk):
    m=Period.objects.get(id=pk)
    if(m.Free_Period_Taken_By != 'None'):
        m.Free=False
        m.save()
        return redirect('Details')
    return render(request,'Takefree.html')
def schedule(request):
    dest=Period.objects.all()
    per=Period.objects.all()
    return render(request,'schedule.html',{'dest':dest,'per':per})

def details(request):
    dest=Details.objects.all()
    return render(request,'nav.html',{'dest':dest})

def updateMessages(request,pk):
    m=Details.objects.get(id=pk)
    form_class=Messages
    form=Messages(instance=m)
    if request.method=='POST':
        form=Messages(request.POST,instance=m)
        if form.is_valid():
            form.save()
            return redirect('Details')
    context={'form':form}
    return render(request,'message.html',context)

def takePeriod(request):
    per=Period.objects.all()
    return render(request,'addFree.html',{'per':per})

'''def takePeriodH(request,pk):
    m=Period.objects.get(id=pk)
    m.Free_Period_Taken_By=request.user
    m.save()
    return redirect('Details')'''

def takePeriodH(request,pk):
    m=Period.objects.get(id=pk)
    det=Details.objects.get(Name=request.user)
    det2=Details.objects.get(Name=m.Free_Period_Taken_By)
    pt1=det.Reserve_Points
    pt2=0
    if(det2):
        pt2=det2.Reserve_Points
    if(det2 and pt1 < pt2):
        return render(request,'addH.html',{'pt1':pt1,'pt2':pt2})
    else:
        temp=m.Free_Period_Taken_By
        m.Free_Period_Taken_By=request.user
        m.save()
        return render(request,'addH.html',{'m':m,'pt1':pt1,'pt2':pt2})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department_contact.html')

def delete(request):
    per=Period.objects.filter(Name=request.user,Free=True).values()
    print(per)
    class temp:
        def __init__(self,name,day,time,id):
         self.name=name 
         self.day=day
         self.time=time
         self.id=id
    if per:
        x=[]
        for p in per:
            d=Days.objects.get(id=p.get('Day_id'))
            n=User.objects.get(id=p.get('Free_Period_Taken_By_id'))
            t=p.get('Time')
            i=p
            tem=temp(n,d,t,i)
            x.append(tem)
        zipped=zip(x,per)
        return render(request,'delete.html',{'z':zipped})
    else:
       messages.info(request, 'You do not have any free Periods')
    return render(request,'delete.html')
    '''if per:
            print(per)
            for p in per:
                print(p.get('Day_id'))
            return render(request,'delete.html',{'per':per})'''
    

def deleteH(request,pk):
    per=Period.objects.get(id=pk)
    m=Details.objects.get(Name=request.user)
    m.Reserve_Points=m.Reserve_Points-1
    m.save()
    per.Free=False
    per.save()
    return render(request,'deleteH.html')