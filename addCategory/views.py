from django.shortcuts import render,redirect
from .forms import cateGoryForm
# Create your views here.
def addCategory(request):
    pageName='Add Category'

    if request.method=='POST':
        category=cateGoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('addCategory')

    else:
        category=cateGoryForm()
    return render(request,'addCategory.html',{'pageName':pageName,'category':category})
