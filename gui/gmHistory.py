# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmHistory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gmHistory(object):
    def setupUi(self, gmHistory):
        gmHistory.setObjectName("gmHistory")
        gmHistory.resize(798, 490)
        self.gridLayout = QtWidgets.QGridLayout(gmHistory)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(gmHistory)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(gmHistory)
        QtCore.QMetaObject.connectSlotsByName(gmHistory)

    def retranslateUi(self, gmHistory):
        _translate = QtCore.QCoreApplication.translate
        gmHistory.setWindowTitle(_translate("gmHistory", "Group Message History"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("gmHistory", "Team Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("gmHistory", "Send Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("gmHistory", "Message"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gmHistory = QtWidgets.QDialog()
    ui = Ui_gmHistory()
    ui.setupUi(gmHistory)
    gmHistory.show()
    sys.exit(app.exec_())
"""
