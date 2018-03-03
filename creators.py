from youtubemissingvideonotify import checklinks
from youtubemissingvideonotify import youtubegetter
from youtubemissingvideonotify import keys

channel_id = input("Whats your channel playlist ID?")
youtubegetter.channels[channel_id] = {"email": "test@gmail.com"}
videos = youtubegetter.fetch_videos(api_key=keys.key,channel_id=channel_id)
youtubegetter.makeCSV(videos)
checklinks.checkLinks("Video_list.csv")

