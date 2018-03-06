from youtubemissingvideonotify import checklinks
from youtubemissingvideonotify import youtubegetter
from youtubemissingvideonotify import keys

#### Setup
channel_id = input("Whats your channel playlist ID?")
youtubegetter.channels[channel_id] = {"email": "test@gmail.com"}
videos = youtubegetter.fetch_videos(api_key=keys.key,channel_id=channel_id)
youtubegetter.makeCSV(videos)



#### main system


#todo cronjob
checklinks.checkLinks("Video_list.csv")

