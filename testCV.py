# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:25:44 2018

@author: Andre
"""

import cv2
import os
dirname='C:\FrameData\ReceptionEast'

cap = cv2.VideoCapture("rtsp://admin:1qazxsw2!QAZXSW@@datascience.opswerx.org:20043")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame) #records video
    cv2.imshow('frame', frame) #displays original video
    #cv2.imshow('gray', gray) #displays gray-ed out video
    
    ##saves each frame as an image in the directory "dirname"
    name = "rec_frame"+str(count)+".jpg"
    cv2.imwrite(os.path.join(dirname,name), frame)
    count+=1
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()