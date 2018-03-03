from youtubemissingvideonotify import checklinks
from youtubemissingvideonotify import youtubegetter
from youtubemissingvideonotify import keys

videos = youtubegetter.fetch_videos(api_key=keys.key,channel_id=input("whats your channel id?"))
youtubegetter.makeCSV(videos)
checklinks.checkLinks("Video_list.csv")

