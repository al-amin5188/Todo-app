from django.shortcuts import render, redirect
from todoapp.models import TodoApp
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):

    task= TodoApp.objects.all()
    return render(request,'todoapp/index.html', {'task' : task})

@login_required
def addtask(request):

    if request.method=='POST':
        title = request.POST.get('title')
        detels = request.POST.get('detels')
        time= request.POST.get('time')

        #add data
        new_task= TodoApp(
            title=title,
            detels=detels,
            time=time
        )

        new_task.save()

        return redirect('')

    return render (request,'todoapp/addtask.html')


def delete (request,id):
    mem=TodoApp.objects.get(id=id)
    mem.delete()


    return redirect('')

def Update(request,id ):
    task=TodoApp.objects.get(id=id)

    if request.method=='POST':
        title = request.POST.get('title')
        detels = request.POST.get('detels')
        time= request.POST.get('time')

        #update task
        task.title=title
        task.detels=detels
        task.time=time

        task.save()

        return redirect('')


    return render(request,'todoapp/updatetask.html',{'task': task})


