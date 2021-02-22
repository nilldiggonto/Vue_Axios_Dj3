from django.forms import ModelForm
from django import forms
from .models import Category,Bookmark

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title','description')

    #add a custom class or id
    # def __init__(self,*args,**kwargs):
    #     super(CategoryForm,self).__init__(*args,**kwargs)
    #     self.fields['title'].widget.attrs['class'] = 'name'
    #     self.fields['description'].widget.attrs['id']='something'


class BookmarkForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Bookmark
        fields = ('title','description','url')
     