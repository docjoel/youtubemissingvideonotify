from django.test import TestCase
from YT_model.models import You_TubeChannel
# Create your tests here.

class ChannelModelTest(TestCase):


    channel = You_TubeChannel("UUVykYhKkOLuIKVr7F0b1npg", "Unmedicated and Dysfunctional", 297, 0)
    channel.save()

    def test_build(self):

        self.assertEqual(self.channel.channelName, "Unmedicated and Dysfunctional")


    def test_addVideo(self):
        self.assertEqual(self.channel.number_of_videos,297)
        self.channel.update_video_count(298)
        self.assertEqual(self.channel.number_of_videos,298)
        self.assertEqual(self.channel.number_of_old_videos,297)


    def test_missing(self):
        self.channel.update_video_count(280)
        self.assertEqual(self.channel.video_missing,True)




