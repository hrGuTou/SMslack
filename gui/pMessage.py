# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pMessage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pmHistory import *
import sys
sys.path.append('../gui')
import control


class Ui_pMessage(object):
    def setupUi(self, pMessage):
        pMessage.setObjectName("pMessage")
        pMessage.resize(549, 440)
        pMessage.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(pMessage)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(pMessage)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(pMessage)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(pMessage)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 4)
        self.label = QtWidgets.QLabel(pMessage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(pMessage)
        self.comboBox.setObjectName("comboBox")
        personName = control.names()
        self.comboBox.addItems(personName)

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(pMessage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(pMessage)
        QtCore.QMetaObject.connectSlotsByName(pMessage)

        # ui connect 
        self.pushButton.clicked.connect(self.clickedSend)
        self.pushButton_2.clicked.connect(self.clickedPmHistory)



        
    def retranslateUi(self, pMessage):
        _translate = QtCore.QCoreApplication.translate
        pMessage.setWindowTitle(_translate("pMessage", "Personal Message"))
        self.pushButton.setText(_translate("pMessage", "Send"))
        self.pushButton_2.setText(_translate("pMessage", "Message History"))
        self.label.setText(_translate("pMessage", "Enter your message:"))
        self.label_2.setText(_translate("pMessage", "Select a person to send message:"))

    def clickedSend(self):
        msg=self.plainTextEdit.document().toPlainText()
        target = [str(self.comboBox.currentText())]
        control.sendPM(msg,target)


    def clickedPmHistory(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_pmHistory()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()



"""
if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     pMessage = QtWidgets.QDialog()
     ui = Ui_pMessage()
     ui.setupUi(pMessage)
     pMessage.show()
     sys.exit(app.exec_())
"""
