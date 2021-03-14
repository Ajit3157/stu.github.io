from django.shortcuts import render
from .forms import  studentreg
from django.http  import HttpResponseRedirect
from.models import user


def delete(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def edit(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
     pi=user.objects.get(pk=id)
     fm=studentreg(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
     
def addshow(request):
    if request.method=='POST':
        fm=studentreg(request.POST)
        if fm.is_valid():
            fm.save()
            fm=studentreg()
    else:
     fm=studentreg()
    stud=user.objects.all()
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud})

# Create your views here.
