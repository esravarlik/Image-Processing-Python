import cv2
import numpy as np

cap = cv2.VideoCapture(0)
knn = cv2.createBackgroundSubtractorKNN()
#mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    mask = knn.apply(frame)

    cv2.imshow('Mask',mask)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


