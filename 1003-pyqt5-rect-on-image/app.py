import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Image Example'
        self.init_gui()
    
    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 640, 480)

        self.label = QLabel(self)
        self.pixmap = QPixmap('road.jpg')
        self.label.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self.pixmap)
        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.drawRect(200, 200, 240, 200)
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())
