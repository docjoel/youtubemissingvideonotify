from django.test import TestCase
from .models import You_TubeChannel
# Create your tests here.

class ChannelModelTest(TestCase):


    channel = You_TubeChannel("UUVykYhKkOLuIKVr7F0b1npg", "Unmedicated and Dysfunctional", 297, 0)
    channel.save()

    def test_build(self):

        self.assertIs(self.channel.channelName == "Unmedicated and Dysfunctional")


