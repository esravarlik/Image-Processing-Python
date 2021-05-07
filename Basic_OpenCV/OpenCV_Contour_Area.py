import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gaus = cv2.GaussianBlur(frame,(5,5),0)
    hsv = cv2.cvtColor(gaus,cv2.COLOR_BGR2HSV)

    #Blue
    lower_blue = np.array([38,86,0])
    upper_blue = np.array([121,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            cv2.drawContours(frame,i,-1,(255,0,0),3)

    cv2.drawContours(frame,contours,-1,(255,0,0),3)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()