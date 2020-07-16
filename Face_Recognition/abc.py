import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 0 is for webcam
cap = cv2.VideoCapture(0)  

while True:
    _,img = cap.read()
# img = cv2.imread('img1.jpeg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

        # The loop terminates as soon as the escape key is pressed

cap.release()