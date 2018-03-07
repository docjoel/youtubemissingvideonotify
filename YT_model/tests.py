from django.test import TestCase
from .models import *
# Create your tests here.
class ChannelModelTest(TestCase):


    def setUp(self):
       channel = You_TubeChannel("UUVykYhKkOLuIKVr7F0b1npg", "Unmedicated and Dysfunctional", 297, 0)
