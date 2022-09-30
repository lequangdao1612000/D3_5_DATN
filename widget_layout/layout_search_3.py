# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'layout_setup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Layout_Search(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
            
    def setupUi(self):
        self.setObjectName("Search")
        self.resize(1000, 500)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txt_plate = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_plate.sizePolicy().hasHeightForWidth())
        self.txt_plate.setSizePolicy(sizePolicy)
        self.txt_plate.setObjectName("txt_plate")
        self.gridLayout_2.addWidget(self.txt_plate, 0, 1, 1, 1)
        self.qlabel_plate = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_plate.sizePolicy().hasHeightForWidth())
        self.qlabel_plate.setSizePolicy(sizePolicy)
        self.qlabel_plate.setObjectName("qlabel_plate")
        self.gridLayout_2.addWidget(self.qlabel_plate, 0, 0, 1, 1)
        self.qlabel_color = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_color.sizePolicy().hasHeightForWidth())
        self.qlabel_color.setSizePolicy(sizePolicy)
        self.qlabel_color.setObjectName("qlabel_color")
        self.gridLayout_2.addWidget(self.qlabel_color, 2, 0, 1, 1)
        self.txt_color = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_color.sizePolicy().hasHeightForWidth())
        self.txt_color.setSizePolicy(sizePolicy)
        self.txt_color.setObjectName("txt_color")
        self.gridLayout_2.addWidget(self.txt_color, 2, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 3, 1, 1, 1)
        self.txt_brand = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_brand.sizePolicy().hasHeightForWidth())
        self.txt_brand.setSizePolicy(sizePolicy)
        self.txt_brand.setObjectName("txt_plate")
        self.gridLayout_2.addWidget(self.txt_brand, 1, 1, 1, 1)
        self.btn_apply = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy)
        self.btn_apply.setObjectName("btn_apply")
        self.gridLayout_2.addWidget(self.btn_apply, 3, 0, 1, 1)
        self.qlabel_brand = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_brand.sizePolicy().hasHeightForWidth())
        self.qlabel_brand.setSizePolicy(sizePolicy)
        self.qlabel_brand.setObjectName("qlabel_brand")
        self.gridLayout_2.addWidget(self.qlabel_brand, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("background: white")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 314, 273))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaWidgetContents.setStyleSheet("background: black")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Search", "Search"))
        self.groupBox.setTitle(_translate("self", "GroupBox"))
        self.qlabel_plate.setText(_translate("self", "Plate"))
        self.qlabel_color.setText(_translate("self", "Color"))
        self.btn_cancel.setText(_translate("self", "Hủy bỏ"))
        self.btn_apply.setText(_translate("self", "Chấp nhận"))
        self.qlabel_brand.setText(_translate("self", "Brand"))


if __name__ == "__main__":
    import sys
    from layout_info_car import Ui_Info_Car
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Layout_Search()
    ui.show()
    
    for i in range(10):
        ui_info_car = Ui_Info_Car()
        ui.scrollAreaWidgetContents.layout().addWidget(ui_info_car)
    
    sys.exit(app.exec_())

