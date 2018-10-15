import cv2
import numpy as np

pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.rectangle(pic, (0, 0), (500, 150), (123, 200, 93), 3, lineType=8, shift=0)
cv2.line(pic, (300, 300), (500, 350), (0, 0, 255))
cv2.circle(pic, (250, 250), 50, (255, 0, 255))
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(pic, 'Suchat S', (100, 100), font, 3, (255, 255, 255), 4, cv2.LINE_8)
cv2.imshow('dark', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
