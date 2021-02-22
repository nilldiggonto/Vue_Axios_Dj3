from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category,Bookmark

@csrf_exempt
def api_delete_category(request,cat_id):
    category = request.user.categories.all().get(pk=cat_id)
    category.delete()

    return JsonResponse({'success':True})