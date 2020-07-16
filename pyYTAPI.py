import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

# the api key is in the windows environment's path area. You are calling it from OS with it's name
api_key = os.environ.get("YOUTUBE_API_KEY")

# youtuberName = input()

yt_service = build("youtube", "v3", developerKey=api_key)

# request = yt_service.channels().list(
#    part='contentDetails, statistics',
#    forUsername=youtuberName
# )
# moonmoon's channel id UCykE3qY-wFLmUMSuryhnS1g
# ch_pl_request = yt_service.playlists().list(
#    part='contentDetails, snippet',
#    channelId="UCykE3qY-wFLmUMSuryhnS1g"
# )

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0
nextPageToken = None
while True:
    pl_items_request = yt_service.playlistItems().list(
        part='contentDetails',
        playlistId="PLF9AzKys0492RIcAJjZBIcoqNUtZ6kt79",
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_items_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    # print(','.join(vid_ids))

    vid_request = yt_service.videos().list(
        part='contentDetails',
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        hours = int(hours.group(1)) if hours else 0
        minutes = minutes_pattern.search(duration)
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = seconds_pattern.search(duration)
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        total_seconds += video_seconds
        # print("{}H {}M {}S".format(hours, minutes, seconds))
        # print(video_seconds)
        # print()

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print("This Playlist is {}H {}M {}S in Total".format(hours, minutes, seconds))
