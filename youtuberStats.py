import os
from googleapiclient.discovery import build

api_key = os.environ.get("YOUTUBE_API_KEY")

print("This script will return to you stats of a youtuber. Enter in the youtuber's name.")
youtuberName = input()

yt_service = build('youtube', 'v3', developerKey=api_key)

request = yt_service.channels().list(
    part='contentDetails, statistics',
    forUsername=youtuberName
)

response = request.execute()
print(response)

# response_viewCount = response['viewCount']
# print(response_viewCount)
