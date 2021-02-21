from django.forms import ModelForm
from django import forms
from .models import Category,Bookmark

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title','description')


class BookmarkForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Bookmark
        fields = ('title','description','url')
     