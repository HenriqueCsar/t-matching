from PIL import ImageGrab
import numpy as np
import cv2

##IMPLEMENTAR LOGO, MAIS TARDE AQUI
template = cv2.imread("henrique.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

while(True):
    img = ImageGrab.grab(bbox=(300,100,800,800))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()