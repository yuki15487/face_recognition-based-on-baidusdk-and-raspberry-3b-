# -*- coding: utf-8 -*-

import time
from picamera import PiCamera
import base64
import requests
import json
from datetime import datetime

def getImage():
    with PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        time.sleep(2)
        camera.capture('face1001.jpg')
        time.sleep(2)
#take a photo

access_token = '' #get your own access_token and fill in it

getImage()
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
with open("face1001.jpg", 'rb') as f: #just have same filename as in getImage()
        image = base64.b64encode(f.read())
body = {
    "image": image,
    "image_type": "BASE64",
    "group_id_list": "1001", # groupId could be set in baidu account.
    "quality_control": "LOW",
    "liveness_control": "NORMAL",
    "match_threshold": "80",
}
headers = {"Content-Type": "application/json"}
request_url = f"{request_url}?access_token={access_token}"
response = requests.post(request_url, headers=headers, data=body)
content = response.content.decode("UTF-8")
print(content) #print in terminal and you can call any param you want
