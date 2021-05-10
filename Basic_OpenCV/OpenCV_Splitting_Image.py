import cv2

image=cv2.imread("umr_image.png")

#band = blue, green, red
b,g,r =cv2.split(image)

new_image=cv2.merge((r,g,b)) #False Color

image[:,:,0]=255
image[:,:,1]=255
image[:,:,2]=255


cv2.imshow("Blue Image:",b)
cv2.imshow("Green Image:",g)
cv2.imshow("Red Image:",r)
cv2.imshow("New_Image",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()