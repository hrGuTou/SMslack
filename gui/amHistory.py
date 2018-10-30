# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amHistory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_amHistory(object):
    def setupUi(self, amHistory):
        amHistory.setObjectName("amHistory")
        amHistory.resize(743, 512)
        self.gridLayout = QtWidgets.QGridLayout(amHistory)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(amHistory)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(amHistory)
        QtCore.QMetaObject.connectSlotsByName(amHistory)

    def retranslateUi(self, amHistory):
        _translate = QtCore.QCoreApplication.translate
        amHistory.setWindowTitle(_translate("amHistory", "Announcement History"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("amHistory", "Send Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("amHistory", "Message"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    amHistory = QtWidgets.QDialog()
    ui = Ui_amHistory()
    ui.setupUi(amHistory)
    amHistory.show()
    sys.exit(app.exec_())

"""