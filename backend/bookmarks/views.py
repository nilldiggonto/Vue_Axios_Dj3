from django.shortcuts import render

# Create your views here.
def bookmarkView(request):
    template_name = 'bookmarks/bookmark.html'
    return render(request,template_name)