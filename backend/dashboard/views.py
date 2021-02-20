from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bookmarks.models import Bookmark
# Create your views here.

@login_required
def dashboardView(request):
    template_name = 'dashboard/dashboard.html'
    bookmarks = Bookmark.objects.filter(added_by = request.user)

    context = {
        'bookmarks':bookmarks,
    }
    return render(request,template_name,context)
