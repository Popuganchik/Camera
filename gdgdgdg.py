import numpy as np
import cv2


cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.color_BGR2GRAY)
    cv2.imshow('1', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindow('1')

