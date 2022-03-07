import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_red = np.array([0, 50, 50])
    high_red = np.array([10, 255, 255])

    red_mask = cv2.inRange(hsv,low_red,high_red)
    red = cv2.bitwise_and(frame,frame,mask = red_mask)

    circles = cv2.HoughCircles(red_mask, cv2.HOUGH_GRADIENT, 1.5, 700, param1=100, param2=20)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (255, 0, 0), 3)
            cv2.circle(frame, (x, y), 1, (255, 0, 0), 3)
            print("X coor:", x)
            print("Y coor:", y)
    else:
        x = 0
        y = 0
        print(x, y)
        
    cv2.imshow("red",red)
    cv2.imshow("frame", red_mask)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(20)
    if key == 27:
        break