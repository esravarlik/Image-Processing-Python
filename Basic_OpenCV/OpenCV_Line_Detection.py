import cv2
import numpy as np

img = cv2.imread("umr_image.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,75,150)
line = np.pi/180
lines = cv2.HoughLinesP(edges,1,line,50)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

cv2.imshow("Canny",edges)
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
