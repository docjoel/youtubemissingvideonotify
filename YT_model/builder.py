from .models import *
import datetime
from .youtubegetter import *



"""

This builds both the initial channels
and the inital video list


"""





"""

channelName = models.CharField(max_length=ChannelNameLength)
    number_of_videos = models.IntegerField()
    number_of_old_videos = models.IntegerField()

"""

channel_list = []


def add_channel_init(key,channel_id):
    # builds and adds channel to channel list
    channel= You_TubeChannel(channel_Id=channel_id,
                                               number_of_videos=fetch_channel(api_key=key,channel_id=channel_id)["Video Count"],
                                               number_of_old_videos=fetch_channel(api_key=key,channel_id=channel_id)["Video Count"])

    channel.save()

video_list = []
def add_video_init(key,channel_id):

    """
    videoID = models.CharField(max_length=YTVideoID,primary_key=True)
    reference_to_channel = models.ForeignKey(to=You_TubeChannel)
    published_date = models.DateTimeField()
    name = models.CharField(max_length=ChannelNameLength)
    existed = models.BooleanField()
    last_found = models.DateTimeField()
    :param channel_id:
    :return:
    """
    for channel in channel_list:
        temp_video_list = fetch_videos(api_key=key,channel_id=channel_id)
        try:
            for show in temp_video_list:
                youttubemovie = Video(videoID=show,reference_to_channel=channel,published_date=show[1]["Time published"],
                                      name=show[0]["title of video"],existed=True,last_found=datetime.datetime)
                youttubemovie.save()
        except:
            print("Something went wrong")





