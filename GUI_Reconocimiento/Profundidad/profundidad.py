import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import os

cap = cv2.VideoCapture(0)
execution_path = os.getcwd()
imgTeoria = cv2.imread(os.path.join(execution_path , "Profundidad/img.png"))
detector = FaceMeshDetector(maxFaces=1)
 
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
 
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Dibujo de lineas usadas para el calculo de profundidad
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3
 
        # # Largo del focal
        # d = 50
        # f = (w*d)/W
        # print(f)

        # Distancia
        f = 840
        d = (W * f) / w
        print(d)
 
        cvzone.putTextRect(img, f'Profundidad: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)
    cv2.imshow("Teoria para el calculo de profundidad", imgTeoria)
    cv2.imshow("Calculo de profundidad (S para Salir)", img)
    if cv2.waitKey(1)==ord('s'):
        break
cap.release()
cv2.destroyAllWindows()