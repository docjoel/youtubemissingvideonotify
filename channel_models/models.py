from django.db import models
from django.contrib.postgres import fields


YTVideoID = 11
YTChannelID= 32
ChannelNameLength = 100

class Channel(models.Model):
    """
    represents a channel

    """

    channelID = models.CharField(max_length=YTChannelID,primary_key=True)
    channelName = models.CharField(max_length=ChannelNameLength)
    number_of_videos = models.IntegerField()

    def to_dictionary(self):
        return {"channelID": Channel.channelID, "Channel Name": Channel.channelName,
                "Number of Videos":Channel.number_of_videos}



class Video(models.Model):
    """
    represents a movie
    """

    videoID = models.CharField(max_length=YTVideoID,primary_key=True)
    reference_to_channel = models.ForeignKey(to=Channel)
    published_date = models.DateTimeField()
    name = models.CharField(max_length=ChannelNameLength)
    existed = models.BooleanField()
    last_found = models.DateTimeField()

    def to_dictionary(self):
        return {"Video ID":Video.videoID,"Name":Video.name,"published date":Video.published_date,"exists":Video.existed}



