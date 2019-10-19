import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):

    def __init__(self):
        super().__init__()        
        self.setWindowTitle('Window Example')
        self.move(300, 300)
        self.resize(400, 300)
        self.show()

app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())
