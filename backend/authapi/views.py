from django.shortcuts import render
from .models import Posts
from .serializers import PostSerializers

from rest_framework import generics
from rest_framework.response import Response
# Create your views here.

class PostView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializers(queryset,many=True)
        return Response(serializer.data)
