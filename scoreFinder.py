import requests
import json
import datetime
import random
import time
import tweepy

osuToken = os.environ['osu']
auth = tweepy.OAuthHandler(os.environ['tAPI'], os.environ['tSecret'])
auth.set_access_token(os.environ['tAccess'], os.environ['tAccessSecret'])
api = tweepy.API(auth)

def findRandomMap(): #time is in epoch starting from ranked date in epoch of Disco Prince
    timeMap = datetime.datetime.fromtimestamp(random.randint(1191692790,int(time.time())-86400)).strftime('%Y-%m-%d %H:%M:%S')
    beatmapsetID = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&since={timeMap}&limit=1&m=0").json()[0]['beatmapset_id']
    data = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&s={beatmapsetID}&m=0").json()
    data = data[random.randint(0,len(data)-1)]
    title = data['title']
    difficulty = data['version']
    return data['beatmap_id']

def getTitle(mapID):
    return requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&b={mapID}").json()[0]['title']

def getDif(mapID):
    return requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&b={mapID}").json()[0]['version']
 
def findRandomScore(mapID):
    data = requests.get(f"https://osu.ppy.sh/api/get_scores?k={osuToken}&b={mapID}&limit=100").json()
    print(data)
    print(mapID)
    return data[random.randint(0,len(data)-1)]

while True:
    map = findRandomMap()
    score = findRandomScore(map)
    api.update_status(f"{score['username']} played {getTitle(map)} [{getDif(map)}] and got {score['pp']} pp on {score['date']} UTC.")
    time.sleep(3600)