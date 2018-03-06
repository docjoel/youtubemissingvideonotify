from django.db import models
from django.contrib.postgres import fields


YTVideoID = 11
YTChannelID= 32
ChannelNameLength = 100

class channel(models.Model):
    """
    represents a channel

    """

    channelID = models.CharField(max_length=YTChannelID)
    channelName = models.CharField(max_length=ChannelNameLength)
    number_of_videos = models.IntegerField()
