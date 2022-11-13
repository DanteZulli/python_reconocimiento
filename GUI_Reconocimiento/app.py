import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import winsound

execution_path = os.getcwd()


# Clase Principal
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi((os.path.join(execution_path, "GUI_Reconocimiento.ui")), self)
        self.setWindowIcon(QIcon(os.path.join(execution_path, "GUI_Imagenes/python.png")))
        # ToolTips
        self.btnFacial.setToolTip("Un programa que reconoce <b>rostros</b> y los compara con una base de datos.")
        self.btnContornos.setToolTip("Un programa que reconoce y contabiliza <b>contornos</b> específicos.")
        self.btnObjetos.setToolTip(
            "Un programa que reconoce distintos <b>objetos/entidades</b> y los encuadra, junto a un porcentaje de "
            "aproximación. <br> <b>NOTA: TARDA EN EJECUTARSE.</b>")
        self.btnManos.setToolTip("Un programa que reconoce <b>gestos hechos con las manos</b> y los interpreta.")
        self.btnPose.setToolTip("Un programa que reconoce <b>tus poses y movimientos.</b>")
        self.btnMascara.setToolTip(
            "Un programa que reconoce <b>tu rostro</b> y genera una máscara de él, registrando así todas tus gesticulaciones.")
        self.btnPiedraPapelTijeras.setToolTip(
            "El clásico piedra, papel y tijeras contra la IA. <b>Podrás vencerla?</b>")
        self.btnEntornoVirtual.setToolTip(
            "Un pequeño proyecto de un <b>entorno virtual</b> que utiliza Python, Unity y C#.")
        self.btnMovimientos.setToolTip("Un detector con alarma que reconoce <b>movimientos</b>.")
        self.btnCaracteristicas.setToolTip("Un programa que reconoce <b>características</b> por aproximación según tu rostro.")
        self.btnVolumen.setToolTip("Un pequeño programa para controlar el <b>volumen</b> de tu PC con gestos de la mano.")
        self.btnDistancias.setToolTip("Un programa que reconoce la <b>distancia</b> entre tu mano y la cámara por medio de cálculos matemáticos.")
        self.btnProfundidad.setToolTip("Un programa que reconoce la <b>profundidad</b> de tu rostro por medio de cálculos matemáticos.")
        # Botones
        self.btnFacial.clicked.connect(iniciarFacial)
        self.btnContornos.clicked.connect(iniciarContornos)
        self.btnObjetos.clicked.connect(iniciarObjetos)
        self.btnMenu.clicked.connect(self.moverMenu)
        self.btnManos.clicked.connect(iniciarManos)
        self.btnPose.clicked.connect(iniciarPose)
        self.btnMascara.clicked.connect(iniciarMascara)
        self.btnPiedraPapelTijeras.clicked.connect(iniciarPiedraPapelTijeras)
        self.btnEntornoVirtual.clicked.connect(iniciarEntornoVirtual)
        self.btnMovimientos.clicked.connect(iniciarMovimientos)
        self.btnCaracteristicas.clicked.connect(iniciarCaracteristicas)
        self.btnVolumen.clicked.connect(iniciarVolumen)
        self.btnDistancias.clicked.connect(iniciarDistancias)
        self.btnProfundidad.clicked.connect(iniciarProfundidad)

    def moverMenu(self):
        if True:
            width = self.frDesplegable.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frDesplegable, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Salir', "¿Está seguro de que desea salir?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def iniciarFacial():
    exec(open(os.path.join(execution_path, "Facial/facial.py")).read())

def iniciarProfundidad():
    exec(open(os.path.join(execution_path, "Profundidad/profundidad.py")).read())

def iniciarVolumen():
    exec(open(os.path.join(execution_path, "Volumen/volumen.py")).read())

def iniciarMovimientos():
    exec(open(os.path.join(execution_path, "Movimientos/movimientos.py")).read())


def iniciarDistancias():
    exec(open(os.path.join(execution_path, "Distancias/distancias.py")).read())

def iniciarCaracteristicas():
    exec(open(os.path.join(execution_path, "Caracteristicas/caracteristicas.py")).read())

def iniciarEntornoVirtual():
    exec(open(os.path.join(execution_path, "EntornoVirtualManos/Main.py")).read())


def iniciarPiedraPapelTijeras():
    exec(open(os.path.join(execution_path, "PiedrasPapelTijeras/juegoPiedraPapelTijeras.py")).read())


def iniciarMascara():
    exec(open(os.path.join(execution_path, "FacialMascara/facialMascara.py")).read())


def iniciarPose():
    exec(open(os.path.join(execution_path, "Pose/pose.py")).read())


def iniciarManos():
    exec(open(os.path.join(execution_path, "Manos/manos.py")).read())


def iniciarObjetos():
    exec(open(os.path.join(execution_path, "Objetos/objetos.py")).read())


def iniciarContornos():
    exec(open(os.path.join(execution_path, "Contornos/contornos.py")).read())


# Checkeo funcion Main para abrir, cerrar o minimizar
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
