import sys
import io
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor



class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.draw_button.clicked.connect(self.paint)
        self.update()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = randint(10, 500)
        qp.drawEllipse(randint(0, 600), randint(50, 300), radius, radius)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec_())
