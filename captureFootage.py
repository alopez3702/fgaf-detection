# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:25:44 2018

@author: Andre
"""

import cv2
import os
dirnameTrue='C:\FrameData\ReceptionWest' #directory where images will be stored
url = "C:\FrameData\ReceptionWestVideo.mp4" #directory to video or feed you want to take images from
cap = cv2.VideoCapture(url)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
count = 0
saveTrue = False
def draw_event(event, x, y, flags, param):
    global saveTrue, saveFalse
    if event == 1: #on left mouse click
        saveTrue=True
    if event == 4: #on left mouse release
        saveTrue=False

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    out.write(frame) #records video
    cv2.imshow('frame', frame) #displays original video
    cv2.setMouseCallback('frame', draw_event, 0) #detect mouse click
    
    #saves each frame as an image in the directory "dirname"
    name = "rec_frame"+str(count)+".jpg"
    if(saveTrue):
        cv2.imwrite(os.path.join(dirnameTrue,name), frame)
        count+=1
    if cv2.waitKey(20) & 0xFF == ord('q'): #press q to shutdown recording
        break
cap.release()
out.release()
cv2.destroyAllWindows()