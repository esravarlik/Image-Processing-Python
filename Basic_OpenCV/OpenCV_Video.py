#Video_Open_CV
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# 0 = Webcam
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == 27:
        # 27 = ESC
        break
cap.release()
cv2.destroyAllWindows()