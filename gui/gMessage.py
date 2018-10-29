# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gMessage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gMessage(object):
    def setupUi(self, gMessage):
        gMessage.setObjectName("gMessage")
        gMessage.resize(566, 395)
        self.gridLayout = QtWidgets.QGridLayout(gMessage)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(gMessage)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(gMessage)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(gMessage)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(gMessage)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(gMessage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(gMessage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.retranslateUi(gMessage)
        QtCore.QMetaObject.connectSlotsByName(gMessage)

    def retranslateUi(self, gMessage):
        _translate = QtCore.QCoreApplication.translate
        gMessage.setWindowTitle(_translate("gMessage", "Group Message"))
        self.pushButton.setText(_translate("gMessage", "Send"))
        self.pushButton_2.setText(_translate("gMessage", "Message History"))
        self.label_2.setText(_translate("gMessage", "Select a team to send message:"))
        self.label.setText(_translate("gMessage", "Enter your message:"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gMessage = QtWidgets.QDialog()
    ui = Ui_gMessage()
    ui.setupUi(gMessage)
    gMessage.show()
    sys.exit(app.exec_())
"""
