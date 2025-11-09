# -*- coding: utf-8 -*-
"""
Created on Sat Nov 8 4:31:30 2025

@author: MALHAR DAVE
"""

import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue
    
    cv2.imshow("video frame",frame)
  
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if key_pressed == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    