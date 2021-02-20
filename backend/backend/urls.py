
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authapi.urls')),
    path('bookmark/',include('bookmarks.urls')),
    path('dashboard/',include('dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)

