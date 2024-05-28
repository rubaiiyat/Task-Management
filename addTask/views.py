from django.shortcuts import render,redirect
from .forms import addForm
from .import models
# Create your views here.
def addTask(request):
    pageName='Add Task'
    
    if request.method=='POST':
        form=addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addTask")
        
    else:
        form=addForm()
    return render(request,'addTask.html',{'pageName':pageName,'form':addForm})

def editPost(request,id):
    pageName='Edit Post'
    
    post=models.addTask.objects.get(pk=id)
    editForm=addForm(instance=post)
    if request.method=='POST':
       editForm=addForm(request.POST,instance=post)
       if editForm.is_valid():
            editForm.save()
            return redirect("home")
        
    
    return render(request,'addTask.html',{'pageName':pageName,'form':editForm})



def deleteTask(request,id):
    delete=models.addTask.objects.get(pk=id).delete()
    return redirect('home')
    