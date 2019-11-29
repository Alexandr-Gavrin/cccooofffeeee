import sys
from random import randint
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(432, 378)
        self.pb = QtWidgets.QPushButton(Form)
        self.pb.setGeometry(QtCore.QRect(120, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb.setFont(font)
        self.pb.setObjectName("pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb.setText(_translate("Form", "Сгенерировать"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        draw.ellipse((x, y, x + l, y + l), (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.new_image.save('res.png', "PNG")
        self.pixmap = QPixmap('res.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
