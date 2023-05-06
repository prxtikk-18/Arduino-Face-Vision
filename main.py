import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('COM12')

while True:
    success, img = cap.read()
    # returns bounding boxes for the face
    img, bBoxes = detector.findFaces(img)

    if bBoxes:
        arduino.sendData([1, 0])
    else:
        arduino.sendData([0, 1])
    cv2.imshow("Video", img)
    cv2.waitKey(1)