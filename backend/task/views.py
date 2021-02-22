from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def taskHome(request):
    return render(request,'task/task.html')


# class TaskView(View):

#     def get(self)