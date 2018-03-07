from django.shortcuts import render

# Create your views here.


from rest_framework import generics

from .models import *
from .serializers import *

class video_list(generics.ListCreateAPIView):
    """
    Lists all Videos
    """
    queryset = Video.objects.all()
    serializer_class = Video_Serializer

class Channel_List(generics.ListCreateAPIView):
    """
    Lists all Videos
    """
    queryset = You_TubeChannel.objects.all()
    serializer_class = You_TubeChannel_Serializer


