from rest_framework import serializers
from .models import Posts

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['post','content']