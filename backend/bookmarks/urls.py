from django.urls import path
from .views import (bookmarkView,SignupView,categoriesView,categoryDetailView,categoryAddView,
                        bookmarkAddView,categoryEditView,category_delete,bookmarkEditView,bookmark_delete)
from django.contrib.auth import views

from .api import api_delete_category
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
    path('category/bookmark/<int:cat_id>/<int:book_id>/',bookmarkEditView,name='bookmark-edit'),
    path('category/bookmark/delete/<int:cat_id>/<int:book_id>/',bookmark_delete,name='bookmark-delete'),


    path('api/delete_category/<int:cat_id>/',api_delete_category,name='api_delete_category'),

]