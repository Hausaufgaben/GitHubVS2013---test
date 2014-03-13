#https://github.com/Hausaufgaben/GitHubVS2013.git
#https://github.com/SmAaMyA/GitHubVS2013---test.git

import sys
from PySide.QtGui import *
from PySide.QtCore import *

'''
class Simple_drawing_window(QWidget):
	def __init__ (self):
		QWidget.__init__(self, None)
		self.setWindowTitle("Simple Drawing")
		self.rabbit = QImage("images/rabbit.png")

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)

		p.setPen(QColor(0, 0, 0))
		p.setBrush(QColor(0, 127, 0))
		p.drawPolygon([QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)])
		p.setPen(QColor(255, 127, 0))
		p.setBrush(QColor(255, 127, 0))
		p.drawPie(50, 150, 100, 100, 0, 180 * 16)

		p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)])

		p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
		p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 1")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(400, 50), QPoint(200, 250), QPoint(600, 250)])

        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 2")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPie(50, 50, 200, 200, 0, 360 * 16)

        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 3")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 128))
        p.drawPolygon([QPoint(200, 50), QPoint(200, 250), QPoint(600, 250), QPoint(450,50)])
        p.end()
'''

def main():
    app = QApplication(sys.argv);

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())