from django.urls import path
from .views import (bookmarkView,SignupView,categoriesView,categoryDetailView,categoryAddView,
                        bookmarkAddView,categoryEditView,category_delete)
from django.contrib.auth import views
urlpatterns = [
    path('',bookmarkView,name='bookmark-page'),
    path('signup/',SignupView,name='bookmark-signup'),
    path('login/',views.LoginView.as_view(template_name='bookmarks/login.html'),name='bookmark-login'),
    path('logout/',views.LogoutView.as_view(),name='bookmark-logout'),


    path('category/add/',categoryAddView,name='bookmark-category-add'),


    path('category/',categoriesView,name='bookmark-category'),
    path('category/edit/<int:id>/',categoryEditView,name='bookmark-category-edit'),
    path('category/delete/<int:id>/',category_delete,name='bookmark-category-delete'),

    path('category/<int:id>/',categoryDetailView,name='bookmark-category-detail'),

    path('category/bookmark/<int:id>/',bookmarkAddView,name='bookmark-add'),
]