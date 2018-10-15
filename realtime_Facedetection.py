import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
leye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
reye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

#pic = cv2.imread('photo.jpg')
pic = cv2.imread('david.jpg')
#pic = cv2.imread('ying.jpg')
#vdocapture = cv2.VideoCapture(0)
scale_factor = 1.3

while 1:
    #ret, pic = vdocapture.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = pic[y:y+h, x:x+w]

        cv2.rectangle(pic, (x, y), (x+w, y+h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'Ying', (x, y), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

        #leye = leye_cascade.detectMultiScale(roi_gray)
        leye = leye_cascade.detectMultiScale(roi_color)
        for (ex, ey, ew, eh) in leye:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    print("Number of face found {}".format(len(faces)))
    cv2.imshow('face', pic)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()
