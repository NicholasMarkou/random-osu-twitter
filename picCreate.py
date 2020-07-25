import requests
import json
import datetime
import random
import time
import tweepy
import os
from PIL import Image, ImageOps, ImageFont, ImageDraw
from Score import *

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

randomScore = Score()
print(randomScore.getTitle())
#Beatmap cover image
BCover = Image.open(requests.get(randomScore.getMapThumbnailURL(), stream=True).raw)
#Profile Picture
PPic = ImageOps.expand(Image.open(requests.get(randomScore.getProfPicURL(), stream=True).raw).resize((100,100)),border=3,fill='black')
BCover.paste(PPic, (10,10))
draw = ImageDraw.Draw(BCover)
shadowText(draw,124,5,randomScore.userScore['username'],ImageFont.truetype("arial.ttf", 22))
shadowText(draw,124,30,'#'+randomScore.player['pp_rank'],ImageFont.truetype("arial.ttf", 22))
shadowText(draw,124,55,'pp: '+randomScore.player['pp_raw'],ImageFont.truetype("arial.ttf", 22))
shadowText(draw,124,80,randomScore.player['accuracy'][0:5]+"%",ImageFont.truetype("arial.ttf", 22))
shadowText(draw,'center',210,f"{randomScore.map['artist']} - {randomScore.map['title']} [{randomScore.map['version']}]",ImageFont.truetype("arial.ttf", 24))
shadowText(draw,800,12,randomScore.map['difficultyrating'][0:4]+'*',ImageFont.truetype("arial.ttf", 16))
shadowText(draw,800,30,'AR: '+randomScore.map['diff_approach'],ImageFont.truetype("arial.ttf", 16))
shadowText(draw,800,48,'OD: '+randomScore.map['diff_overall'],ImageFont.truetype("arial.ttf", 16))
shadowText(draw,800,66,randomScore.map['bpm']+' BPM',ImageFont.truetype("arial.ttf", 16))
BCover.show()