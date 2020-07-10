import os
from googleapiclient.discovery import build

# the api key is in the windows environment's path area. You are calling it from OS with it's name
api_key = os.environ.get("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=api_key)
