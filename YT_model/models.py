from django.db import models
from django.contrib.postgres import fields
# Create your models here.

YTVideoID = 11
YTChannelID= 32
ChannelNameLength = 100

class You_TubeChannel(models.Model):
    """
    represents a channel

    """
    channelID = models.CharField(max_length=YTChannelID,primary_key=True)
    channelName = models.CharField(max_length=ChannelNameLength)
    number_of_videos = models.IntegerField()
    number_of_old_videos = models.IntegerField()
    def __repr__(self):
        return str(self.identifier)
    def to_dictionary(self):
        return {"channelID": You_TubeChannel.channelID, "Channel Name": You_TubeChannel.channelName,
                "Number of Videos":You_TubeChannel.number_of_videos}



class Video(models.Model):
    """
    represents a movie
    """

    videoID = models.CharField(max_length=YTVideoID,primary_key=True)
    reference_to_channel = models.ForeignKey(to=You_TubeChannel)
    published_date = models.DateTimeField()
    name = models.CharField(max_length=ChannelNameLength)
    existed = models.BooleanField()
    last_found = models.DateTimeField()
    def __repr__(self):
        return str(self.identifier)
    def to_dictionary(self):
        return {"Video ID":Video.videoID,"Name":Video.name,"published date":Video.published_date,"exists":Video.existed}