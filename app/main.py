import base64

import cv2
import numpy as np
from fastapi import FastAPI, Request

from app.hog import gethog

app = FastAPI()

def readb64(uri):
    encoded_data = uri.split(",")[1]
    nparr = np.fromstring(base64.b64decode(encoded_data),np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img

@app.post("/api/gethog")
async def read_str(request: Request):
    try:
        data = await request.json()
        img = readb64(data.get("item_str"))
        hog = gethog(img)
        return {"HOG": hog.tolist()}
    except Exception as e:
        return {"error" : str(e)}













# @app.get("/api/genhog")
# def getthog(img_gray):
#     data_split = img_gray.split(',',1) 
#     # ตัด data ถึง base64 เพื่อให้ได้ข้อมูลภาพ
#     data = data_split[1] 
#     decode_imgData = base64.b64decode(data) 
#     decode_img = cv2.imdecode(np.frombuffer(decode_imgData,np.uint8),cv2.IMREAD_GRAYSCALE)
#     s = (128,128)
#     resize_img = cv2.resize(decode_img,s,cv2.INTER_AREA)
#     win_size = resize_img.shape
#     cell_size = (8, 8)
#     block_size = (16, 16)
#     block_stride = (8, 8)
#     num_bins = 9
#     # Set the parameters of the HOG descriptor using the variables defined above
#     hog = cv2.HOGDescriptor(win_size, block_size, block_stride,
#     cell_size, num_bins)
#     # Compute the HOG Descriptor for the gray scale image
#     hog_descriptor = hog.compute(resize_img)
#     hog_descriptorList = hog_descriptor.flatten().tolist()
#     # print ('HOG Descriptor:', hog_descriptor)
#     return {"hogvector":hog_descriptorList}