from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Category,Bookmark
from .forms import CategoryForm,BookmarkForm


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
def categoryAddView(request):
    template_name = 'bookmarks/category-add.html'
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.added_by = request.user
            category.save()

            return redirect('bookmark-category')
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,template_name,context)


#edit
@login_required
def categoryEditView(request,id):
    template_name = 'bookmarks/category-edit.html'
    catForm = Category.objects.filter(added_by=request.user).get(pk=id)
    form = CategoryForm(request.POST,instance=catForm)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=catForm)

        if form.is_valid():
            # category = form.save(commit=False)
            form.save()
            # category.added_by = request.user
            # category.save()

            return redirect('bookmark-category')
    else:
        form = CategoryForm(instance=catForm)
    context = {
        'form':form,
        'catForm':catForm,
    }
    return render(request,template_name,context)


@login_required
def categoriesView(request):
    template_name = 'bookmarks/categories.html'
    category = Category.objects.filter(added_by=request.user)
    context = {
        'category':category,
    }
    return render(request,template_name,context)


### BOOKMARK UNDER CATEGORy
@login_required
def categoryDetailView(request,id):
    # TimeoutError
    template_name= 'bookmarks/category-detail.html'
    category = Category.objects.get(pk=id)

    context = {
        'cat':category,
    }
    return render(request,template_name,context)



@login_required
def category_delete(request,id):
    category = Category.objects.filter(added_by=request.user).get(pk=id)
    # categoriesView
    category.delete()
    return redirect('bookmark-category')










##bookmark add
@login_required
def bookmarkAddView(request,id):
    template_name = 'bookmarks/bookmark-add.html'
    category = Category.objects.get(pk=id)
    form = BookmarkForm()
    if request.method == 'POST':
        form = BookmarkForm(request.POST)

        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.added_by = request.user
            bookmark.category_id = id
            bookmark.save()

            return redirect('bookmark-category-detail',id=id)
    else:
        form = BookmarkForm()
    context = {
        'form':form,
        'category':category,
    }
    return render(request,template_name,context)


#bookmark EDIT
@login_required
def bookmarkEditView(request,cat_id,book_id):
    template_name = 'bookmarks/bookmark_update.html'
    category = Category.objects.get(pk=cat_id)

    bookmark_e = Bookmark.objects.filter(added_by=request.user).get(pk=book_id)
    # form = BookmarkForm(request.POST, instance=bookmark_e)
    if request.method == 'POST':
        form = BookmarkForm(request.POST,instance=bookmark_e)

        if form.is_valid():
            # bookmark = form.save(commit=False)
            # bookmark.added_by = request.user
            # bookmark.category_id = id
            form.save()

            return redirect('bookmark-category-detail',id=cat_id)
    else:
        form = BookmarkForm(instance=bookmark_e)
    context = {
        'form':form,
        'category':category,
        'bookmark':bookmark_e,
    }
    return render(request,template_name,context)


@login_required
def bookmark_delete(request,cat_id,book_id):
    bookmark = Bookmark.objects.filter(added_by=request.user).get(pk=book_id)
    # categoriesView
    bookmark.delete()
    return redirect('bookmark-category-detail', id=cat_id)



