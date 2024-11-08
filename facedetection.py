import cv2
data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("img3.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = data.detectMultiScale(gray,1.3,5)
for(x,y,w,h)in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
cv2.imshow("FaceDetection",img)

