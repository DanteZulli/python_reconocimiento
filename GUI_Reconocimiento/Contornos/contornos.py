#Contador de monedas (Eliminacion de ruido y Eliminacion de ruido interno)
import cv2
import numpy as np #Libreria de informatica cientifica
import os
execution_path = os.getcwd()

valorGauss=3
valorKernel=3 #GAUSS Y KERNEL SIEMPRE MATRICES IMPARES
#Se puede jugar con estos valores subiendo y bajando para aumentar o disminuir la intensidad de busqueda de contornos y ruido

imagen=cv2.imread(os.path.join(execution_path , "Contornos/monedas.jpg"))
original=cv2.imread(os.path.join(execution_path , "Contornos/monedas.jpg"))
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

#ELIMINACION DE RUIDO
#Contornos mas exactos (Gauss Blur)(Suavizado)
gauss=cv2.GaussianBlur(gris,(valorGauss,valorGauss),0) #Siempre debe ser una matriz de tipo igual
#Teoría de Canny (Segunda eliminacion de ruidos)
canny=cv2.Canny(gauss,60,100)

#ELIMINACION DE RUIDO INTERNO
kernel=np.ones((valorKernel,valorKernel),np.uint8) #Entero de 8bits
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

#Busca contornos despues de limpiar el ruido interno
contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#Cuenta contornos
cv2.drawContours(original,contornos,-1,(0,0,255),2)

#Proceso de muestreo de contornos
cv2.imshow('Original (Espacio para ver la siguiente imagen)',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Grises (Paso 1) (Espacio para ver la siguiente imagen)',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Gauss (Paso 2) (Espacio para ver la siguiente imagen)',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Canny (Paso 3) (Espacio para ver la siguiente imagen)',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Reconocimiento Contornos (S para volver al menu)",original)
cv2.waitKey(0)
cv2.destroyAllWindows()