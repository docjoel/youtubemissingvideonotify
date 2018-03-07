from youtubemissingvideonotify import keys
from youtubemissingvideonotify.channel_models import checklinks, youtubegetter

#### Setup
channel_id = input("Whats your channel playlist ID?")
youtubegetter.channels[channel_id] = {"email": "test@gmail.com"}
videos = youtubegetter.fetch_videos(api_key=keys.key, channel_id=channel_id)
youtubegetter.makeCSV(videos)



#### main system


#todo cronjob
checklinks.checkLinks("Video_list.csv")

