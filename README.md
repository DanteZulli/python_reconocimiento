# python_reconocimiento
## Descripción General y Consideraciones
Este es mi proyecto de reconocimiento con Python<br>
Lo hice para la "Muestra Anual de Saberes y Capacidades Profesionales 2022" de la Escuela de Educación Secundaria Técnica N°2 (E.E.S.T N°2 Temperley).<br>
Cuenta con varios proyectos que ponen en práctica los conceptos de Inteligencia Artificial, Redes Neuronales, Aprendizaje de Máquina y Visión Computacional entre otras cosas.<br>
La interfaz fue realizada con QT, más especificamente PyQt5. El código fuente de la interfaz se encuentra en el archivo "GUI_Reconocimiento.ui" ya que lo hice con QT DESIGNER. Las imágenes que usé se encuentran en la carpeta GUI_Imagenes.<br>
Si no me equivoco, debería de ser completamente compatible con Qt6. Sin embargo, pienso implementarlo en PySide2, ya que es de libre uso comercial. (No es compatible nativamente, ya que las animaciones del menú desplegable no funcionan).<br>
El proyecto esta hecho con Python 3.7.9 por comodidad, ya que uno de los proyectos usaba librerías depreciadas. Luego me encontré con que gran parte de las librerías no se encontraban en Python 3.11. El Downgrade a Python 3.7.9 fue por comodidad, ya que no quería tener que cambiar el código de los proyectos. Pienso solventar esto en un futuro, subiendolo aunque sea a Python 3.9.x.<br>
Fue realizado con VSCODE, con las configuraciones default.<br>
No utilicé un entorno virtual de ningun tipo, ya que me olvidé de configurarlo al inicio. El proyecto iba a ser algo simple que terminé escalando, y cuando me quise dar cuenta ya era demasiado tarde.<br>
Recientemente conseguí licencia de PyCharm Professional gracias al proyecto de Github Education, así que ni bien pueda, lo voy a migrar a un entorno virtual, de preferencia en este IDE, y así conseguir un requirements.txt como corresponde. (Si alguien tiene una idea de como hacerlo, por favor, que me avise).<br>
El proyecto de Entorno Virtual Manos (La parte que mas convenció al publico) sigue en desarrollo aparte. En este repositorio se encuentra la carpeta con uno de los prototipos ya compilados (Para más comodidad a la hora de presentarlo). El código todavía no tiene repositorio propio, ya que lo empecé de cero. (El código de ese futuro repositorio es el mismo que el presentado en la muestra, pero con algunas cosas agregadas y más ideas implementadas).<br>
NOTA: Agregué el archivo "requirements.txt" para que sea más fácil de instalar las librerías necesarias. (No es el archivo original, ya que no tengo el entorno virtual, lo hice con pipreqs en VSCode).
## Licencia MIT
Decidí utilizar la licencia MIT, ya que es una licencia bastante permisiva, y me permite utilizarla en proyectos comerciales. (No estoy seguro de si es compatible con la licencia de Qt, pero no creo que haya problemas).<br>
Es uno de mis primeros proyectos, y no estoy seguro de si es la mejor licencia para este tipo de proyectos. Simplemente quería elegir una licencia de software libre lo suficientemente permisiva para que quien desee, pueda aportar al proyecto. Si alguien tiene una idea de como mejorarla, por favor, que me avise. <br>
## Algunas fotos del proyecto y de la expo
Por alguna razón, sacaron foto de mi stand justo cuando yo no estaba, así que no tengo foto presentándolo. (No me importa, pero me hubiera gustado tener una foto como recuerdo :') ).
[![Reconocimiento.jpg](https://i.postimg.cc/0NpyT67M/Reconocimiento.jpg)](https://postimg.cc/Lq8Sf8C2)
[![315447491-505311208285894-5866838246486971973-n.jpg](https://i.postimg.cc/KYvmH9cV/315447491-505311208285894-5866838246486971973-n.jpg)](https://postimg.cc/RWyr3LHQ)
## Proyectos
### Reconocimiento de Características
Este proyecto consiste en un reconocimiento de características a partir de el análisis del rostro de las personas.<br>
Para esto se utilizaron las librerias de OpenCV, MediaPipe y DeepFace principalmente.<br>
Calcula el Género, la Edad, la Emoción y la Raza de la persona.
### Reconocimiento de Distancias
Este proyecto consiste en un reconocimiento de distancias a partir de cuentas matemáticas aproximadas, en base a la distancia entre dos puntos de la mano del usuario.<br>
Se utilizó el modulo de HandTracking de CVZONE y OpenCV para el reconocimiento de la mano.
### Reconocimiento de Contornos
Este proyecto consiste en un reconocimiento de contornos a partir de el análisis de una imagen deseada.<br>
Fue realizado con la libreria de OpenCV, para explicar el proceso de reconocimiento que realiza la computadora.
### Entorno Virtual Manos
La obra Magna de la presentación.<br>
Este proyecto consiste en un entorno virtual a partir de el reconocimiento de la mano del usuario.<br>
Es un proyecto de reconocimiento en python, con un entorno virtual a modo de "Juego" hecho en Unity3D.<br>
Se comunican via UDP (Protocolo de comunicación de red).<br>
Tiene algunos scripts realizados en C# para el control de frames, y el envío e interpretación de los datos.<br>
Se utilizó el modulo de HandTracking de CVZONE y OpenCV para el reconocimiento de la mano.<br>
NOTA: El proyecto de Unity esta ya compilado dentro de la carpeta "Entorno Virtual Manos". Pienso agregar el repositorio más adelante.<br>
NOTA2: No tengo mucha idea de como utilizar Unity sinceramente, fue algo simpe que hice para la muestra. Se aceptan sugerencias.<br>
Fue inspirado en Minecraft en honor a mi hermanita Ámbar que es fanática de ese juego.
### Reconocimiento Facial
Este proyecto consiste en un reconocimiento facial sencillo.<br>
Lo realicé con OpenCV, para demostrar como se puede realizar un reconocimiento facial sencillo y personalizarlo.
### Reconocimiento Facial Mascara
Este proyecto consiste en un reconocimiento facial con mascarilla.<br>
Lo realicé con OpenCV, para demostrar como se puede realizar un reconocimiento facial con mascarilla.
### Reconocimiento de Manos
Este proyecto consiste en un reconocimiento de manos y los gestos de las mismas. <br>
Utilice un modelo ya entrenado que tiene algunos gestos registrados (Los mismos se encuentran en el archivo gestos.names).<br>
Lo realicé con OpenCV, MediaPipe y TensorFlow, para demostrar como se puede realizar un reconocimiento de manos y los gestos de las mismas.
### Reconocimiento de Movimientos
Este proyecto consiste en un reconocimiento de movimientos en la cámara, y una simple "alarma" integrada.<br>
Lo realicé con OpenCV y algunas librerías extras para el sonido.
### Piedra Papel Tijeras
Pequeño juego de Piedra Papel y Tijeras contra la IA.<br>
Utiliza OpenCV y el HandTrackingModule de CVZONE.
### Reconocimiento de Poses
Este proyecto consiste en un reconocimiento de la pose del cuerpo humano.<br>
Lo realicé con OpenCV y MediaPipe.
### Reconocimiento de Objetos
Este proyecto consiste en un reconocimiento de objetos a partir de una imagen.<br>
Lo realice con ImageAi. Una libreria depreciada ya que usa el modelo "resnet50_coco_best_v2.1.0.h5".<br>
Este modelo no se encuentra en la carpeta del proyecto ya que pesa demasiado, lo pueden conseguir en internet. (Si no lo encuentran me piden link, aunque pienso cambiar esto, así no se requiere más este modelo)<br>
Es la principal razón por la que utilicé python 3.7.9 ya que no se puede instalar ImageAi en python 3.8 o superior.<br>
(Se que fue un error de mi parte, pienso solventarlo más adelante)
### Reconocimiento de Profundidad
Este proyecto consiste en un reconocimiento de profundidad a partir de cálculos matemáticos entre la distancia de dos puntos de la cara.<br>
Lo realice con OpenCV y el FaceMeshModule de CVZONE.
### Control de Volumen
Este proyecto consiste en un control de volumen a partir de la distancia entre los dedos.<br>
Lo realice con OpenCV y MediaPipe y PyCaw, entre otras librerías.

