from rest_framework import serializers
from .models import *


class You_TubeChannel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = You_TubeChannel
        fields = "__all__"

class Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
