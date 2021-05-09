import cv2
import numpy as np

image = cv2.imread("umr_image.png",0)

print(image.size) #pixel count
print(image.dtype) #uints8,uints16
print(image.item(100, 100), 0) 
print(image.item(100, 100), 1)
print(image.item(100, 100), 2)
print(image.shape) #width, height, band size

cv2.rectangle(image,(1000,550),(600,150),[0,0,255],2) #(x,y),(x,y)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
