from django.shortcuts import render,redirect
from django.views.generic import View

from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def taskHome(request):
    return render(request,'task/task.html')


class TaskView(View):

    def get(self,request):
        tasks = list(Task.objects.values())

        

        context = {
            'tasks':tasks,
        }
        if request.is_ajax():
            return JsonResponse(context,status=200)

        return render(request,'task/task.html',context)

    
    def post(self,request):
        bound_form = TaskForm(request.POST)
        if bound_form.is_valid():
            new_task = bound_form.save()

            return JsonResponse({'tasks':model_to_dict(new_task)}, status=200)

        return redirect('task')
