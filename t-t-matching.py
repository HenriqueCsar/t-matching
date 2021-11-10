from PIL import ImageGrab
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('face.xml')

while(True):
	img = ImageGrab.grab(bbox=(300,100,800,800))
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
	