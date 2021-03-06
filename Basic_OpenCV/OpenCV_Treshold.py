import cv2
import numpy as np

def nothing(x):
    pass

image = cv2.imread("umr_image.png", 0)
image = cv2.resize(image, (320,240))
cv2.namedWindow("Image")
cv2.createTrackbar("Threshold value", "Image", 140, 255, nothing)

while True:

    value_threshold = cv2.getTrackbarPos("Threshold value", "Image")
    _, threshold_binary = cv2.threshold(image, value_threshold, 255, cv2.THRESH_BINARY)
    _, threshold_binary_inv = cv2.threshold(image, value_threshold, 255, cv2.THRESH_BINARY_INV)
    _, threshold_trunc = cv2.threshold(image, value_threshold, 255, cv2.THRESH_TRUNC)
    _, threshold_to_zero = cv2.threshold(image, value_threshold, 255, cv2.THRESH_TOZERO)
    _, threshold_to_zero_inv = cv2.threshold(image, value_threshold, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow("Image", image)
    cv2.imshow("th binary", threshold_binary)
    cv2.imshow("th binary inv", threshold_binary_inv)
    cv2.imshow("th trunc", threshold_trunc)
    cv2.imshow("th to zero", threshold_to_zero)
    cv2.imshow("th to zero inv", threshold_to_zero_inv)

    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()