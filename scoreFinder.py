import requests
import json
import datetime
import random
import time
import tweepy
import os
from PIL import Image, ImageOps, ImageFont, ImageDraw
from Score import *

auth = tweepy.OAuthHandler(os.environ['tAPI'], os.environ['tSecret'])
auth.set_access_token(os.environ['tAccess'], os.environ['tAccessSecret'])
api = tweepy.API(auth)

def shadowText(draw,x,y,text,font):
    if x == 'center':
        w,h=draw.textsize(text,font)
        x=(900-w)/2
    shadowcolor='black'
    #Border
    draw.text((x-1, y), text, font=font, fill=shadowcolor)
    draw.text((x+1, y), text, font=font, fill=shadowcolor)
    draw.text((x, y-1), text, font=font, fill=shadowcolor)
    draw.text((x, y+1), text, font=font, fill=shadowcolor)
    draw.text((x-1, y-1), text, font=font, fill=shadowcolor)
    draw.text((x+1, y-1), text, font=font, fill=shadowcolor)
    draw.text((x-1, y+1), text, font=font, fill=shadowcolor)
    draw.text((x+1, y+1), text, font=font, fill=shadowcolor)
    #white text
    draw.text((x,y), text, font=font, fill=(255,255,255,255))

while True:
    randomScore = Score()
    #Beatmap cover image
    BCover = Image.open(requests.get(randomScore.getMapThumbnailURL(), stream=True).raw)
    #Profile Picture
    PPic = ImageOps.expand(Image.open(requests.get(randomScore.getProfPicURL(), stream=True).raw).resize((100,100)),border=3,fill=20)
    BCover.paste(PPic, (10,10))
    draw = ImageDraw.Draw(BCover)
    shadowText(draw,10,115,randomScore.userScore['date'],ImageFont.truetype("arial.ttf", 20))
    ranking=Image.open(f"mods/{randomScore.userScore['rank']}.png")
    BCover.paste(ranking, (10,140),ranking)
    shadowText(draw,124,5,randomScore.userScore['username'],ImageFont.truetype("arial.ttf", 22))
    shadowText(draw,124,30,'#'+randomScore.player['pp_rank'],ImageFont.truetype("arial.ttf", 22))
    shadowText(draw,124,55,'pp: '+randomScore.player['pp_raw'],ImageFont.truetype("arial.ttf", 22))
    shadowText(draw,124,80,randomScore.player['accuracy'][0:5]+"%",ImageFont.truetype("arial.ttf", 22))
    shadowText(draw,'center',185,f"{randomScore.map['artist']} - {randomScore.map['title']} [{randomScore.map['version']}]",ImageFont.truetype("arial.ttf", 24))
    shadowText(draw,'center',210,'Mapped by '+randomScore.map['creator'],ImageFont.truetype("arial.ttf", 24))
    shadowText(draw,800,5,randomScore.map['difficultyrating'][0:4]+'*',ImageFont.truetype("arial.ttf", 18))
    shadowText(draw,800,30,'AR: '+randomScore.map['diff_approach'],ImageFont.truetype("arial.ttf", 18))
    shadowText(draw,800,55,'OD: '+randomScore.map['diff_overall'],ImageFont.truetype("arial.ttf", 18))
    shadowText(draw,800,80,randomScore.map['bpm']+' BPM',ImageFont.truetype("arial.ttf", 18))
    BCover.save('score.png','png')
    api.update_with_media('score.png', f"{randomScore.userScore['username']} played {randomScore.map['title']} [{randomScore.map['version']}] and got {randomScore.userScore['pp']} pp on {randomScore.userScore['date']} UTC.")
    time.sleep(3600)