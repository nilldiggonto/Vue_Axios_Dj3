from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Category


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





####### BOOKMARK CATEGORIES
@login_required
def categoriesView(request):
    template_name = 'bookmarks/categories.html'
    category = Category.objects.filter(added_by=request.user)
    context = {
        'category':category,
    }
    return render(request,template_name,context)

@login_required
def categoryDetailView(request,id):
    # TimeoutError
    template_name= 'bookmarks/category-detail.html'
    category = Category.objects.get(pk=id)

    context = {
        'cat':category,
    }
    return render(request,template_name,context)