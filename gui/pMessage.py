# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pMessage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pMessage(object):
    def setupUi(self, pMessage):
        pMessage.setObjectName("pMessage")
        pMessage.resize(549, 440)
        self.gridLayout = QtWidgets.QGridLayout(pMessage)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(pMessage)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(pMessage)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(pMessage)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(pMessage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(pMessage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(pMessage)
        QtCore.QMetaObject.connectSlotsByName(pMessage)

    def retranslateUi(self, pMessage):
        _translate = QtCore.QCoreApplication.translate
        pMessage.setWindowTitle(_translate("pMessage", "Personal Message"))
        self.pushButton.setText(_translate("pMessage", "Send"))
        self.label.setText(_translate("pMessage", "Enter your message:"))
        self.label_2.setText(_translate("pMessage", "Select a person to send message:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pMessage = QtWidgets.QDialog()
    ui = Ui_pMessage()
    ui.setupUi(pMessage)
    pMessage.show()
    sys.exit(app.exec_())

