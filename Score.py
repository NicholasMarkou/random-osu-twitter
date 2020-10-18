import requests, json, datetime, random, time

class Score:
    osuToken = "19b0ce7766326265ce219103703a3eb6231ce1fa"

    def __init__(self): #time is in epoch starting from ranked date in epoch of Disco Prince
        timeMap = datetime.datetime.fromtimestamp(random.randint(1191692790,int(time.time())-86400)).strftime('%Y-%m-%d %H:%M:%S')
        beatmapsetID = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={Score.osuToken}&since={timeMap}&limit=1&m=0").json()[0]['beatmapset_id']
        mapData = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={Score.osuToken}&s={beatmapsetID}&m=0").json()
        self.map = mapData[random.randint(0,len(mapData)-1)]
        allScore = requests.get(f"https://osu.ppy.sh/api/get_scores?k={Score.osuToken}&b={self.map['beatmap_id']}&limit=100").json()
        self.userScore = allScore[random.randint(0,len(allScore)-1)]
        self.player = requests.get(f"https://osu.ppy.sh/api/get_user?k={Score.osuToken}&u={self.userScore['user_id']}&type=id").json()[0]

    def getProfPicURL(self):
        return f"http://s.ppy.sh/a/{self.userScore['user_id']}"

    def getMapThumbnailURL(self):
        return f"https://assets.ppy.sh/beatmaps/{self.map['beatmapset_id']}/covers/cover.jpg"


    #function found on owobot's repo.
    def num_to_mod(self):
        modsNum = int(self.userScore['enabled_mods'])
        mods = []
        if modsNum & 1<<0:   mods.append('NF')
        if modsNum & 1<<1:   mods.append('EZ')
        if modsNum & 1<<3:   mods.append('HD')
        if modsNum & 1<<4:   mods.append('HR')
        if modsNum & 1<<5:   mods.append('SD')
        if modsNum & 1<<9:   mods.append('NC')
        elif modsNum & 1<<6: mods.append('DT')
        if modsNum & 1<<7:   mods.append('RX')
        if modsNum & 1<<8:   mods.append('HT')
        if modsNum & 1<<10:  mods.append('FL')
        if modsNum & 1<<12:  mods.append('SO')
        if modsNum & 1<<14:  mods.append('PF')
        if modsNum & 1<<15:  mods.append('4 KEY')
        if modsNum & 1<<16:  mods.append('5 KEY')
        if modsNum & 1<<17:  mods.append('6 KEY')
        if modsNum & 1<<18:  mods.append('7 KEY')
        if modsNum & 1<<19:  mods.append('8 KEY')
        if modsNum & 1<<20:  mods.append('FI')
        if modsNum & 1<<24:  mods.append('9 KEY')
        if modsNum & 1<<25:  mods.append('10 KEY')
        if modsNum & 1<<26:  mods.append('1 KEY')
        if modsNum & 1<<27:  mods.append('3 KEY')
        if modsNum & 1<<28:  mods.append('2 KEY')
        return mods