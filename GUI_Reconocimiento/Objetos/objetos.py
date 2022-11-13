#Deteccion de Objetos y o entidades en una imagen
#Python 3.7.9
from imageai.Detection import ObjectDetection
import os
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "Objetos/resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "Objetos/obeliscoNoche.jpg"), output_image_path=os.path.join(execution_path , "Objetos/obelisco_nueva.jpg"))
detections2 = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "Objetos/india.jpg"), output_image_path=os.path.join(execution_path , "Objetos/india_nueva.jpg"))

#Carga de la imagen
imagenNuevaObelisco = mpimg.imread( os.path.join(execution_path , "Objetos/obelisco_nueva.jpg"))
imagenOriginalObelisco = mpimg.imread( os.path.join(execution_path , "Objetos/obeliscoNoche.jpg"))
imagenNuevaIndia = mpimg.imread(os.path.join(execution_path, "Objetos/india_nueva.jpg"))
imagenOriginalIndia = mpimg.imread(os.path.join(execution_path, "Objetos/india.jpg"))

f, axarr = plt.subplots(2,2)
f.canvas.set_window_title('Deteccion de Objetos')
axarr[0,0].imshow(imagenOriginalObelisco)
axarr[0,0].set_title('Imagen Original')
axarr[0,1].imshow(imagenNuevaObelisco)
axarr[0,1].set_title('Imagen con Objetos Detectados')
axarr[1,0].imshow(imagenOriginalIndia)
axarr[1,0].set_title('Imagen Original')
axarr[1,1].imshow(imagenNuevaIndia)
axarr[1,1].set_title('Imagen con Objetos Detectados')
plt.show()
os.remove( os.path.join(execution_path , "Objetos/obelisco_nueva.jpg"))
os.remove( os.path.join(execution_path , "Objetos/india_nueva.jpg"))

