from deepface import DeepFace
import cv2
import mediapipe as mp
import os
from time import sleep

execution_path = os.getcwd()

detros = mp.solutions.face_detection
rostros = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)
dibujorostro = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resrostros = rostros.process(rgb)
    if resrostros.detections is not None:
        for rostro in resrostros.detections:
            al, an, c = frame.shape
            box = rostro.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            cv2.rectangle(frame, (xi, yi), (xf, yf), (0, 0, 255), 1)
            # sleep(1)
            info = DeepFace.analyze(rgb, actions=['age', 'gender','race', 'emotion'], enforce_detection= False)
            edad = info['age']
            emociones = info['dominant_emotion']
            raza = info['dominant_race']
            gen = info['gender']
            #Traducciones
            if gen == "Man":
                gen = "Hombre"
            if gen == "Woman":
                gen = "Mujer"
            if emociones == "angry":
                emociones = "Enojo"
            if emociones == "disgust":
                emociones = "Disgusto"
            if emociones == "fear":
                emociones = "Susto"
            if emociones == "happy":
                emociones = "Felicidad"
            if emociones == "sad":
                emociones = "Tristeza"
            if emociones == "surprise":
                emociones = "Sorpresa"
            if emociones == "neutral":
                emociones = "Neutral"
            if raza == "asian":
                raza = "Asia"
            if raza == "indian":
                raza = "India"
            if raza == "black":
                raza = "Negro"
            if raza == "white":
                raza = "Blanco"
            if raza == "middle eastern":
                raza = "Medio oriental"
            if raza == "latino hispanic":
                raza = "Latino hispano"
            cv2.putText(frame, str(gen), (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.putText(frame, str(edad), (60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.putText(frame, str(emociones), (60, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.putText(frame, str(raza), (60, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            
    cv2.imshow(" Deteccion de Caracteristicas (S para Salir) ", frame)

    key = cv2.waitKey(1)
    if key==ord('s'):
        break
cv2.destroyAllWindows()
cap.release()