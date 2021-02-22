from django.urls import path
from .views import taskHome

urlpatterns = [
    path('',taskHome,name='task'),
]