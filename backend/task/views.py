from django.shortcuts import render

# Create your views here.
def taskHome(request):
    return render(request,'task/task.html')