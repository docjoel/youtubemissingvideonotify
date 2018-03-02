# Example Channel: Kenz - Unmedicated & Dysfunctional
import requests
import json
yt_api_key = "AIzaSyCZF8zzud9yqzDvcrMGbzfBQpJ195HUibA" # YouTube API key goes here
channels = {}
channels["UUVykYhKkOLuIKVr7F0b1npg"] = {"email": "unmedicateddysfunctional@gmail.com"}




# Fetch the latest videos on a channel using the YouTube API.
def fetch_videos(api_key, channel_id, pageToken=None):
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + channel_id + "&key=" + api_key

    if pageToken is not None: base_url = base_url + "&pageToken=" + pageToken

    r = requests.get(base_url)
    page_data = json.loads(r.text)
    videos = {}

    for video in page_data["items"]:
        id = video["snippet"]["resourceId"]["videoId"]
        videos[id] = [{"title of video":video["snippet"]["title"]},{"Time published":video["snippet"]["publishedAt"]}]

        if "pretty_name" not in channels[channel_id]:
            channels[channel_id]["pretty_name"] = video["snippet"]["channelTitle"]

    if "nextPageToken" in page_data:
        add_data = fetch_videos(api_key, channel_id, page_data["nextPageToken"])
        videos.update(add_data)

    return videos


for channel in channels.keys():
    current_channel_videos = fetch_videos(yt_api_key, channel, None)

print(current_channel_videos)


#ToDo need to check if any new videos are in the current channel videos and add them to the CSV

