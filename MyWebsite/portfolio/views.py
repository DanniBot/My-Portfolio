from django.shortcuts import render
from .models import Project, ProjectFilter

# Create your views here.
def homepage(request):
    # projects=Project.objects.all()   #grab all the data from database
    f = ProjectFilter(request.GET, queryset=Project.objects.all().order_by('-priority'))
    groups={}
    for obj in f.qs:
        if obj.topic=='Py':
            groups.setdefault('Py_projects',[]).append(obj)
        if obj.topic=='ML':
            groups.setdefault('ML_projects',[]).append(obj)
        if obj.topic=='Ru':
            groups.setdefault('Ru_projects',[]).append(obj)
        if obj.topic=='PB':
            groups.setdefault('PB_projects',[]).append(obj)
        if obj.topic=='FL':
            groups.setdefault('FL_projects',[]).append(obj)
        if obj.topic=='DJ':
            groups.setdefault('DJ_projects',[]).append(obj)
    return render(request,'portfolio/homepage.html',context=groups)

    # return render(request,'portfolio/homepage.html',{'projects':projects})