import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray,4, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(frame,(x,y),3,[0,0,255],-1)
        #print('x:',x)
        #print('y:',y)

    cv2.imshow('Corner',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()