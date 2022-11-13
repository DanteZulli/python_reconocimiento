import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

#Inicia MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Carga el modelo (Lo baje de un repositorio de github)
model = load_model('Manos/mp_hand_gesture')

# Nombre de los gestos
f = open('Manos/gestos.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Inicia la camara
cap = cv2.VideoCapture(0)

while True:
    # Lee el frame
    _, frame = cap.read()

    x, y, c = frame.shape

    # Convierte el frame a RGB
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detecta las manos
    result = hands.process(framergb)

    className = ''
    # Si detecta una mano
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Dibuja los puntos de la mano
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predice el gesto
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            className = classNames[classID]

    # Muestra el gesto predecido
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Muestra el frame final
    cv2.imshow("Reconocimiento Gestos (S para salir)", frame) 

    if cv2.waitKey(1) == ord('s'):
        break

# Cierra la camara y las ventanas
cap.release()

cv2.destroyAllWindows()