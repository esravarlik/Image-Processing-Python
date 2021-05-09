import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(mask, kernel, iterations=3)
    erosion = cv2.erode(mask, kernel, iterations=3)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #Erosion + Dilation ok.
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #Dilation + Erosion

    cv2.imshow("Image", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
