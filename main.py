import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.new_image = Image.new("RGB", (440, 400), 'white')
        self.new_image.save('res.png', "PNG")
        self.pixmap = QPixmap('res.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(440, 320)
        self.image.setPixmap(self.pixmap)
        self.pb.clicked.connect(self.draw)

    def draw(self):
        draw = ImageDraw.Draw(self.new_image)
        x = randint(0, 440)
        y = randint(0, 320)
        l = randint(0, 100)
        draw.ellipse((x, y, x + l, y + l), 'yellow')
        self.new_image.save('res.png', "PNG")
        self.pixmap = QPixmap('res.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
