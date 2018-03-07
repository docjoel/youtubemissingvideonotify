from django.test import TestCase
from django.utils import timezone
from .models import *


class ChannelTest(TestCase):
    channel = Channel()