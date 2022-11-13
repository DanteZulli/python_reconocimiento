#Librerias Importadas
import cv2  as cv
import numpy as np
import os

execution_path = os.getcwd()

# Base de datos en .XML para detectar rostros (De la librería de OPENCV)
ruidos = cv.CascadeClassifier(os.path.join(execution_path , "Facial/rostrosDB.xml"))
#Captura video y comienza el bucle al detectar la camara
camara = cv.VideoCapture(0)
while True:
    _,captura=camara.read()
    grises = cv.cvtColor(captura,cv.COLOR_BGR2GRAY) #Convierte a grises para facilitar la deteccion
    cara=ruidos.detectMultiScale(grises,scaleFactor=1.3,minNeighbors=5) #Despeja los ruidos de la camara y busca rostros (Imagen origen,Escala de deteccion 1=100%,promedio de contornos)
    #Abre el for con las cordenadas x,y,e1(EsquinaSupIzq) y e2(EsquinaSupDer) para recorrer la camara punto por punto
    for(x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
        cv.putText(captura,'"Tu nombre aqui"',(x,y-20),2,1.1,(0,255,0),1,cv.LINE_AA)

    cv.imshow("Reconocimiento Facial (S para volver al menu)", captura)

    if cv.waitKey(1)==ord('s'):
        break
camara.release()
cv.destroyAllWindows()