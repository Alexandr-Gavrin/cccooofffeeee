import sys
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute('SELECT * FROM coffee')
        self.tableWidget.setColumnCount(7)
        for i, row2 in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, row in enumerate(row2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Сорт',
                                           'Степень обжарки', 'Молотый/в зернах',
                                           'Вкус', 'Цена', 'Объем упаковки'])
        self.tableWidget.resizeColumnsToContents()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
