import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600, height=600, inter=cv2.INTER_AREA)
    #resized = cv2.resize(frame, (600, 600), interpolation=cv2.INTER_LINEAR)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    median = cv2.medianBlur(frame, 5, None)
    opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
    circles = cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1.5, 999, param1=100, param2=80)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(opening, (x, y), r, (0, 0, 255), 3)
            cv2.circle(opening, (x, y), 1, (0, 0, 255), 3)
            print("X coor:", x,end=", ")
            print("Y coor:", y)
    else:
        x = 0
        y = 0
        print(x, y)

    cv2.imshow("Result", opening)

    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()