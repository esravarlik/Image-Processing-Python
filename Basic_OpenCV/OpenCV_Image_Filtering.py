import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    averaging = cv2.blur(frame, (5, 5))
    gaussian = cv2.GaussianBlur(frame, (15,15), 0)
    median = cv2.medianBlur(frame, 5)
    bilateral = cv2.bilateralFilter(frame, 5, 75, 75)

    cv2.imshow("Original Image", frame)
    cv2.imshow("Averaging", averaging)
    cv2.imshow("Gaussian", gaussian)
    cv2.imshow("Median", median)
    cv2.imshow("Bilateral", bilateral)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()