import os
import socket

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Socket es para mandar datos via UDP (UDP = User Datagram Protocol)
# Como un stream continuo para Unity

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
success, img = cap.read()
height, width, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Conexion con Unity C#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
# Ejecucion del Proyecto de Unity
path = os.getcwd()
os.startfile(os.path.join(path , "EntornoVirtualManos/Entorno Virtual.exe"))

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    data = []
    if hands:
        # Detecta la mano y envia los puntos por el puerto
        # Lista de los valores de cada punto (LandMarks)
        lmList = hands[0]['lmList']
        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[2]])
        sock.sendto(str.encode(str(data)), serverAddressPort)
    cv2.imshow("Captura de movimiento (S para Salir)", img)
    if cv2.waitKey(1) == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()

