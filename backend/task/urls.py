from django.urls import path
from .views import taskHome,TaskView

urlpatterns = [
    path('',TaskView.as_view(),name='task'),
]