from django.shortcuts import render
from addTask.models import addTask
def base(request):
    return render (request,'base.html')


def home(request):
    pageName="Home"
    form=addTask.objects.all()
    return render(request,'home.html',{'pageName':pageName,'forms':form})


