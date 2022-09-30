# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_info_car.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(428, 284)
        Form.setStyleSheet("background: green")
        self.qlabel_frame = QtWidgets.QLabel(Form)
        self.qlabel_frame.setGeometry(QtCore.QRect(10, 2, 201, 181))
        self.qlabel_frame.setStyleSheet("background: gray")
        self.qlabel_frame.setObjectName("qlabel_frame")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 190, 31, 21))
        self.label.setStyleSheet("background: gray")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 31, 21))
        self.label_3.setStyleSheet("background: gray")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 31, 21))
        self.label_4.setStyleSheet("background: gray")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 190, 41, 21))
        self.label_5.setStyleSheet("background: gray")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 220, 41, 21))
        self.label_6.setStyleSheet("background: gray")
        self.label_6.setObjectName("label_6")
        self.qlabel_plate = QtWidgets.QLabel(Form)
        self.qlabel_plate.setGeometry(QtCore.QRect(50, 190, 161, 21))
        self.qlabel_plate.setStyleSheet("background: gray")
        self.qlabel_plate.setObjectName("qlabel_plate")
        self.qlabel_color = QtWidgets.QLabel(Form)
        self.qlabel_color.setGeometry(QtCore.QRect(50, 220, 161, 21))
        self.qlabel_color.setStyleSheet("background: gray")
        self.qlabel_color.setObjectName("qlabel_color")
        self.qlabel_brand = QtWidgets.QLabel(Form)
        self.qlabel_brand.setGeometry(QtCore.QRect(50, 250, 161, 21))
        self.qlabel_brand.setStyleSheet("background: gray")
        self.qlabel_brand.setObjectName("qlabel_brand")
        self.qlabel_in_time = QtWidgets.QLabel(Form)
        self.qlabel_in_time.setGeometry(QtCore.QRect(270, 190, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_in_time.sizePolicy().hasHeightForWidth())
        self.qlabel_in_time.setSizePolicy(sizePolicy)
        self.qlabel_in_time.setStyleSheet("background: gray")
        self.qlabel_in_time.setObjectName("qlabel_in_time")
        self.qlabel_out_time = QtWidgets.QLabel(Form)
        self.qlabel_out_time.setGeometry(QtCore.QRect(270, 220, 151, 21))
        self.qlabel_out_time.setStyleSheet("background: gray")
        self.qlabel_out_time.setObjectName("qlabel_out_time")
        self.qlabel_frame_other = QtWidgets.QLabel(Form)
        self.qlabel_frame_other.setGeometry(QtCore.QRect(220, 2, 201, 181))
        self.qlabel_frame_other.setStyleSheet("background: gray")
        self.qlabel_frame_other.setObjectName("qlabel_frame_other")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.qlabel_frame.setText(_translate("Form", "frame"))
        self.label.setText(_translate("Form", "Plate"))
        self.label_3.setText(_translate("Form", "Color"))
        self.label_4.setText(_translate("Form", "Brand"))
        self.label_5.setText(_translate("Form", "In time"))
        self.label_6.setText(_translate("Form", "Out time"))
        self.qlabel_plate.setText(_translate("Form", "qlabel_plate"))
        self.qlabel_color.setText(_translate("Form", "qlabel_color"))
        self.qlabel_brand.setText(_translate("Form", "qlabel_brand"))
        self.qlabel_in_time.setText(_translate("Form", "In time"))
        self.qlabel_out_time.setText(_translate("Form", "Out time"))
        self.qlabel_frame_other.setText(_translate("Form", "frame"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

