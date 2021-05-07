import cv2
import numpy as np

def nothing(x):
    pass

image = np.zeros((300,300,3),np.uint8)

cv2.namedWindow("image")
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)

while True:
    cv2.imshow('image',image)
    k = cv2.waitKey(1)& 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    if r != 0 or g != 0 or b != 0:
        image[:] = [r, g, b]
    else:
        pass
cv2.destroyAllWindows()