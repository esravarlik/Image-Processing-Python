import cv2
import random

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
x = random.randint(1,100)
out = cv2.VideoWriter(str(x) + 'output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()