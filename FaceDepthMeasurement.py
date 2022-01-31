import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import mediapipe
import numpy as np
#find the focal length
from cvzone.FaceMeshModule import FaceMeshDetector
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        #drawing

        #cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        #cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        #cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)

        w,_ = detector.findDistance(pointLeft,pointRight)
        #we are finding the focal length
        W = 6.3 #male
        #d = 50 #assume and set
        #f= (w*d)/W
        #print(f)

        #finding the distance ( depth )
        f = 860
        d=(W*f)/w
        print(d) #distance between camera and face

        cvzone.putTextRect(img,f'Depth:{int(d)}cm',
                           (face[10][0]-100
                            ,face[10][1]-50),
                           scale = 2)




    cv2.imshow("Image", img)
    cv2.waitKey(1)
