import cv2

img = cv2.imread("umr_image.png")
img = cv2.resize(img, (640,480))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_thresh_mean_c = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,5)
adaptive_thresh_gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,5)

cv2.imshow("Image",img)
cv2.imshow("Mean C",adaptive_thresh_mean_c)
cv2.imshow("Gaus",adaptive_thresh_gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()