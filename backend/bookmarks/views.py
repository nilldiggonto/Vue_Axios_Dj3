from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def bookmarkView(request):
    template_name = 'bookmarks/bookmark.html'
    return render(request,template_name)

## Default Signup
def SignupView(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('bookmark-page')
        else:
            form = UserCreationForm()

    template_name = 'bookmarks/signup.html'
    context = {
        'form':form,
    }
    return render(request,template_name,context)