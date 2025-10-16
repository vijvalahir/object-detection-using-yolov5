import torch
import cv2
import time
import os


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
print("Enter no of seconds to record from webcam")
a=input()
a=int(a)
a=a*30
print("Give source of the camera or webcam (Its 0 by default)")
b=input()
b=int(b)

cap = cv2.VideoCapture(b)  

if (cap.isOpened() == False):
    print("Error opening video file")

frames = []
i = 0
while(cap.isOpened()):


    ret, frame = cap.read()
    
    if ret == True:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(image)

        if i == a: 
            break
        else:
           i += 1

    else:
        break
cap.release()


from tqdm import tqdm
result_video = []
for frame in tqdm(frames):
    
    detections = model(frame)
    result_video.append(detections)

h, w, _ = frame.shape
out = cv2.VideoWriter('camout.mp4',cv2.VideoWriter_fourcc(*'mp4v'),30, (w, h)) 
for detection in result_video:
  
    img = detection.render()[0]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    out.write(img)

out.show()
out.release()



