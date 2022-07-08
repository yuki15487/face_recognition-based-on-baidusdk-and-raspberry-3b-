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
        
getImage()

access_token = '' #use your own access_token here

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
body = []
with open("face1001.jpg", 'rb') as f: # file name is same as in getImage()
	image1 = base64.b64encode(f.read()).decode('UTF8')
body1 = {
    "image": image1,
    "image_type": "BASE64",
    "face_type": "LIVE",
    "quality_control": "LOW",
    "liveness_control": "LOW"
}

body.append(body1)
body = json.dumps(body)
headers = {"Content-Type": "application/json"}
request_url = f"{request_url}?access_token={access_token}"
response = requests.post(request_url, headers=headers, data=body)
content = response.content.decode("UTF-8")
# print the response content
print(content)
faceResponse = json.loads(content)
print (faceResponse.get('result').get('face_list'))
faceScore = faceResponse.get('result').get('score')
faceID = faceResponse.get('result').get('face_list')[0].get('face_token')
print(faceID)
if faceScore > 80: #
    print (faceScore)
else:
    print('unknown user! access denied')