from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)

    added_by    = models.ForeignKey(User,related_name='categories', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)  