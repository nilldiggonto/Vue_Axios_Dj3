from django.contrib import admin
from .models import Category,Bookmark
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','added_by','created_at',)


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','added_by','category','created_at')
