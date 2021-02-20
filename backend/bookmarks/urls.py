from django.urls import path
from .views import bookmarkView,SignupView
from django.contrib.auth import views
urlpatterns = [
    path('',bookmarkView,name='bookmark-page'),
    path('signup/',SignupView,name='bookmark-signup'),
    path('login/',views.LoginView.as_view(template_name='bookmarks/login.html'),name='bookmark-login'),
    path('logout/',views.LogoutView.as_view(),name='bookmark-logout'),
]