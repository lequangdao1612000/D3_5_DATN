# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'layout_setup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils_huy_quang.get_search_info import *


class Ui_Layout_Search(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Seach")
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

        # plate
        self.qlabel_plate = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_plate.sizePolicy().hasHeightForWidth())
        self.qlabel_plate.setSizePolicy(sizePolicy)
        self.qlabel_plate.setObjectName("qlabel_plate")
        self.gridLayout_2.addWidget(self.qlabel_plate, 0, 0, 1, 1)

        # txt_plate
        self.txt_plate = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_plate.sizePolicy().hasHeightForWidth())
        self.txt_plate.setSizePolicy(sizePolicy)
        self.txt_plate.setObjectName("txt_plate")
        self.gridLayout_2.addWidget(self.txt_plate, 0, 1, 1, 1)

        # brand
        self.qlabel_brand = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_brand.sizePolicy().hasHeightForWidth())
        self.qlabel_brand.setSizePolicy(sizePolicy)
        self.qlabel_brand.setObjectName("qlabel_brand")
        self.gridLayout_2.addWidget(self.qlabel_brand, 1, 0, 1, 1)

        # txt_brand
        self.txt_brand = QtWidgets.QLineEdit(self.groupBox)
        # completer_brand = QtWidgets.QCompleter(brands, self)
        # completer_brand.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        # self.txt_brand.setCompleter(completer_brand)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_brand.sizePolicy().hasHeightForWidth())
        self.txt_brand.setSizePolicy(sizePolicy)
        self.txt_brand.setObjectName("txt_brand")
        self.gridLayout_2.addWidget(self.txt_brand, 1, 1, 1, 1)

        # color
        self.qlabel_color = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_color.sizePolicy().hasHeightForWidth())
        self.qlabel_color.setSizePolicy(sizePolicy)
        self.qlabel_color.setObjectName("qlabel_color")
        self.gridLayout_2.addWidget(self.qlabel_color, 2, 0, 1, 1)

        # color
        self.txt_color = QtWidgets.QLineEdit(self.groupBox)
        # completer_color = QtWidgets.QCompleter(colors, self)
        # completer_color.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        # self.txt_color.setCompleter(completer_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_color.sizePolicy().hasHeightForWidth())
        self.txt_color.setSizePolicy(sizePolicy)
        self.txt_color.setObjectName("txt_color")
        self.gridLayout_2.addWidget(self.txt_color, 2, 1, 1, 1)
        self.btn_apply = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy)
        self.btn_apply.setObjectName("btn_apply")
        self.gridLayout_2.addWidget(self.btn_apply, 3, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.qlabel_crop_frame = QtWidgets.QLabel(self)
        self.qlabel_crop_frame.setStyleSheet("background: gray""")
        self.qlabel_crop_frame.setObjectName("")
        self.gridLayout.addWidget(self.qlabel_crop_frame, 0, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Search", "Search"))
        self.groupBox.setTitle(_translate("self", "GroupBox"))
        self.qlabel_plate.setText(_translate("self", "Plate"))
        self.qlabel_brand.setText(_translate("self", "Brand"))
        self.qlabel_color.setText(_translate("self", "Color"))
        self.btn_apply.setText(_translate("self", "Chấp nhận"))
        self.btn_cancel.setText(_translate("self", "Hủy bỏ"))
        self.qlabel_crop_frame.setText(_translate("self", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Layout_Search()
    ui.show()
    sys.exit(app.exec_())
