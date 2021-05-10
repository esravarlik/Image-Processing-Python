import cv2
import numpy as np

cap = cv2.VideoCapture("areaonline.mp4")

# Blue color
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])

# Green color
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

#Red color
low_red = np.array([161,155,84])
high_red = np.array([179,255,255])

try:
    while True:
        ret,frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        green_mask = cv2.inRange(hsv, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        red_mask = cv2.inRange(hsv,low_red,high_red)
        red = cv2.bitwise_and(frame,frame,mask = red_mask)

        cv2.imshow("Mask Red",red)
        cv2.imshow("Mask Blue",blue)
        cv2.imshow("Mask Green",green)

        key = cv2.waitKey(10)
        if key == 27:
            break

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()

