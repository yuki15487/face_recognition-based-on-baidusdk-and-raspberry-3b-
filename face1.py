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
#        time.sleep(1)
        camera.capture('face1001.jpg')
#        time.sleep(1)
#take a photo

access_token = '' #use your own access_token here

def detectFace():
    getImage()
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    with open("face1001.jpg", 'rb') as f:
        image = base64.b64encode(f.read())
    body = {
        "image": image,
        "image_type": "BASE64",
    }
    headers = {"Content-Type": "application/json"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")
    faceResponse = json.loads(content)
    if (faceResponse.get('result')):
        faceNumResponse = faceResponse.get('result').get('face_num')
    else:
        faceNumResponse = "0"
    return faceNumResponse

def searchFace():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    with open("face1001.jpg", 'rb') as f:
        image = base64.b64encode(f.read())

    body = {
        "image": image,
        "image_type": "BASE64",
        "group_id_list": "1001",
        "quality_control": "LOW",
        "liveness_control": "NORMAL",
        "match_threshold": "80",
    }
    headers = {"Content-Type": "application/json"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")
    faceResponse = json.loads(content)
    if (faceResponse.get('result')):
        faceUidResponse = faceResponse.get('result').get('user_list')[0].get('user_id')
    else:
        faceUidResponse = ""
    return faceUidResponse

while True: # keep the program running
    publicFaceNumResponse = detectFace()
    time.sleep(2)
    if (publicFaceNumResponse == 1):
        publicFaceUidResponse = searchFace()
        time.sleep(1)
        if (publicFaceUidResponse):
            print ("welcome!",publicFaceUidResponse)
        else:
            print ("unknown user, access denied")
    else: #multi-face detection was not designed
        pass
