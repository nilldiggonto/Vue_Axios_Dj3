from django.urls import path
from .views import bookmarkView
urlpatterns = [
    path('',bookmarkView,name='bookmark-page'),
]