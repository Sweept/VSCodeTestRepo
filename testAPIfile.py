import os
from googleapiclient.discovery import build

api_key = os.environ.get("YOUTUBE_API_KEY")

yt_service = build('youtube', 'v3', developerKey=api_key)

request = yt_service.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)
