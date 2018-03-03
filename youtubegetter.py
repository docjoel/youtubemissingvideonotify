# Example Channel: Kenz - Unmedicated & Dysfunctional
import requests
import json
from youtubemissingvideonotify.keys import key
import csv
import arrow
yt_api_key = key # YouTube API key goes here
channels = {}
channels["UUVykYhKkOLuIKVr7F0b1npg"] = {"email": "test@gmail.com"}


#UUVykYhKkOLuIKVr7F0b1npg

# Fetch the latest videos on a channel using the YouTube API.
def fetch_videos(api_key, channel_id, pageToken=None):
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + channel_id + "&key=" + api_key

    if pageToken is not None: base_url = base_url + "&pageToken=" + pageToken

    r = requests.get(base_url)
    page_data = json.loads(r.text)
    videos = {}
    print(page_data)
    for video in page_data["items"]:
        id = video["snippet"]["resourceId"]["videoId"]
        videos[id] = [{"title of video":video["snippet"]["title"]},{"Time published":video["snippet"]["publishedAt"]}]

        if "pretty_name" not in channels[channel_id]:
            channels[channel_id]["pretty_name"] = video["snippet"]["channelTitle"]

    if "nextPageToken" in page_data:
        add_data = fetch_videos(api_key, channel_id, page_data["nextPageToken"])
        videos.update(add_data)

    return videos



def makeCSV(channelVideos):
    with open("Video_List.csv","w") as outfile:
        columnTitleRow = "video id,Title,date published\n"
        outfile.write(columnTitleRow)
        for video in channelVideos:
            try:
                outfile.write("{0},{1},{2}\n".format(video,str(channelVideos[video][0]["title of video"]).replace(",","")
                                                     ,arrow.get(
                        channelVideos[video][1]["Time published"])).format("MM-DD-YY"))
            except TypeError:
                print("type error")




if __name__ == '__main__':

    for channel in channels.keys():
        current_channel_videos = fetch_videos(yt_api_key, channel, None)

    for video in current_channel_videos:
        print(video,current_channel_videos[video][0]["title of video"],"publsihed at " + arrow.get(current_channel_videos[video][1]["Time published"]).format("MM-DD-YY"))
    makeCSV(current_channel_videos)

#ToDo need to check if any new videos are in the current channel videos and add them to the CSV

