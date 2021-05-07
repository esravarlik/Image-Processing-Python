import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gaus = cv2.GaussianBlur(frame,(5,5),0)
    sobel_x = cv2.Sobel(frame,cv2.CV_64F,1,0)
    sobel_y = cv2.Sobel(frame,cv2.CV_64F,0,1)
    laplacian = cv2.Laplacian(gaus,cv2.CV_64F)
    canny = cv2.Canny(gaus,70,150)

    cv2.imshow("Frame",frame)
    cv2.imshow("Sobel_X",sobel_x)
    cv2.imshow("Sobel_Y", sobel_y)
    cv2.imshow("Laplacian",laplacian)
    cv2.imshow("Canny",canny)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()