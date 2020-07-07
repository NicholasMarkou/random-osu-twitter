import requests
import json
import datetime
import random
import time

osuToken = json.load(open('tokens.json'))['osu']

def findRandomMap(): #time is in epoch starting from ranked date in epoch of Disco Prince
    timeMap = datetime.datetime.fromtimestamp(random.randint(1191692790,int(time.time())-86400)).strftime('%Y-%m-%d %H:%M:%S')
    beatmapsetID = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&since={timeMap}&limit=1").json()[0]['beatmapset_id']
    data = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={osuToken}&s={beatmapsetID}").json()
    return data[random.randint(0,len(data)-1)]['beatmap_id']

def findRandomScore(mapID):
    data = requests.get(f"https://osu.ppy.sh/api/get_scores?k={osuToken}&b={mapID}&limit=100").json()
    return data[random.randint(0,len(data))]


map = findRandomMap()
score = findRandomScore(map)
print(score['score_id'])