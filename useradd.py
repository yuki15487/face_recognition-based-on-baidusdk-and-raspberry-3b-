# -*- coding: utf-8 -*-

import time
import base64
from picamera import PiCamera
import requests
import json
from datetime import datetime
print(datetime.now())

def getImage():
    with PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        time.sleep(2)
        camera.capture('face1001.jpg')
#take a photo

access_token = '' #use your own access_token here

getImage()

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"

with open("face1001.jpg", 'rb') as f:
	image = base64.b64encode(f.read())
userName = input() #input userName in terminal 
body = {
    "image": image,
    "image_type": "BASE64",
    "group_id": "1001",
    "user_id": userName,
    "user_info": "",
    "quality_control": "NONE",
    "liveness_control": "NONE",
}
headers = {"Content-Type": "application/json"}
request_url = f"{request_url}?access_token={access_token}"
response = requests.post(request_url, headers=headers, data=body)
content = response.content.decode("UTF-8")
print(content)
