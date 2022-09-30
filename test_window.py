from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QImage, QPainter, QPen
from PyQt5.QtCore import Qt


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        W, H = 1366, 768
        expand = 2
        MainWindow.resize(W, H)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: white;")

        self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(0, 0, W // 2 - expand, H // 2 - expand))
        self.img1.setObjectName("img1")

        self.img2 = QtWidgets.QLabel(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(W // 2 + expand, 0, W // 2 - expand, H // 2 - expand))
        self.img2.setObjectName("img2")

        self.img3 = QtWidgets.QLabel(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(0, H // 2 + expand, W // 2 - expand, H // 2 - expand))
        self.img3.setObjectName("img3")

        self.img4 = QtWidgets.QLabel(self.centralwidget)
        self.img4.setGeometry(QtCore.QRect(W // 2 + expand, H // 2 + expand, W // 2 - expand, H // 2 - expand))
        self.img4.setObjectName("img4")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys

    # Init QT
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())