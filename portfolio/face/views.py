from django.shortcuts import redirect, render
from .models import *
from .forms import ImageForm
# Create your views here.

def home(request):
    ff=face.objects.all()
    return render(request,'home.html',{'ff':ff})

def my_view(request):
    ff=face.objects.all()

    forms = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    return render(request, 'forms.html', {'forms': forms,'ff': ff})


def detail_view(request,pv):
    projt_view=  face.objects.get(id=pv)  
    return render(request,'project_view.html',{'pr':projt_view})

def delete(request,dlid):
    task=face.objects.get(id=dlid)
    if request.method=="POST":
        task.delete()
        return redirect('face:my_view')
    return render(request,'confrim.html',{'task':task})

