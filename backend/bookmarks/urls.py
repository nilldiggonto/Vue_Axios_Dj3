from django.urls import path
from .views import bookmarkView,SignupView
urlpatterns = [
    path('',bookmarkView,name='bookmark-page'),
    path('signup/',SignupView,name='bookmark-signup'),
]