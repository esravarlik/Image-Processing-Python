#Image_OpenCV
import cv2
image = cv2.imread('umr_image.png')
    #GRAY_SCALE = 0
    #IMREAD_COLOR = 1
    #IMREAD_UNCHANGED = -1
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Image',image)
cv2.imshow('Gray',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()