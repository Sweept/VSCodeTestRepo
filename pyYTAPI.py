import os
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
pl_items_request = yt_service.playlistItems().list(
    part='contentDetails',
    playlistId="PLF9AzKys0492RIcAJjZBIcoqNUtZ6kt79"
)

pl_response = pl_items_request.execute()

vid_ids = []
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])

print(','.join(vid_ids))

vid_request = yt_service.videos().list(
    part='contentDetails',
    id=','.join(vid_ids)
)

vid_response = vid_request.execute()

for item in vid_response['items']:
    print(item)
    print()
