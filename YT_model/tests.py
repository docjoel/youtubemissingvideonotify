from django.test import TestCase
from .models import *
# Create your tests here.
class ChannelModelTest(TestCase):



    channel = You_TubeChannel("UUVykYhKkOLuIKVr7F0b1npg", "Unmedicated and Dysfunctional", 297, 0)


    def test_build(self):

        self.assertIs(self.channel.channelName == "Unmedicated and Dysfunctional")


