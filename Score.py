import requests
import json
import datetime
import random
import time
import os

class Score:
    osuToken = os.environ['osu']

    def __init__(self): #time is in epoch starting from ranked date in epoch of Disco Prince
        timeMap = datetime.datetime.fromtimestamp(random.randint(1191692790,int(time.time())-86400)).strftime('%Y-%m-%d %H:%M:%S')
        beatmapsetID = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={Score.osuToken}&since={timeMap}&limit=1&m=0").json()[0]['beatmapset_id']
        data = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={Score.osuToken}&s={beatmapsetID}&m=0").json()
        self.map = data[random.randint(0,len(data)-1)]
        userScore = requests.get(f"https://osu.ppy.sh/api/get_scores?k={Score.osuToken}&b={self.map['beatmap_id']}&limit=100").json()
        self.userScore = userScore[random.randint(0,len(data)-1)]
        self.player = requests.get(f"https://osu.ppy.sh/api/get_user?k={Score.osuToken}&u={self.userScore['user_id']}&type=id").json()[0]

    def getTitle(self):
        return self.map['title']

    def getDif(self):
        return self.map['version']

    def getUser(self):
        return self.userScore['username']
    
    def getProfPicURL(self):
        return f"http://s.ppy.sh/a/{self.userScore['user_id']}"

    def getMapThumbnailURL(self):
        return f"https://assets.ppy.sh/beatmaps/{self.map['beatmapset_id']}/covers/cover.jpg"