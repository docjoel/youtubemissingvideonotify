from django.apps import AppConfig
class ChannelModelConfig(AppConfig):
    name = 'channel_models'

    def ready(self):
        import channel_models.checklinks
