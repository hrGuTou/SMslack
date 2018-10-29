# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pmHistory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pmHistory(object):
    def setupUi(self, pmHistory):
        pmHistory.setObjectName("pmHistory")
        pmHistory.resize(772, 541)
        self.gridLayout = QtWidgets.QGridLayout(pmHistory)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(pmHistory)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(pmHistory)
        QtCore.QMetaObject.connectSlotsByName(pmHistory)

    def retranslateUi(self, pmHistory):
        _translate = QtCore.QCoreApplication.translate
        pmHistory.setWindowTitle(_translate("pmHistory", "Personal Message History"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("pmHistory", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("pmHistory", "Send Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("pmHistory", "Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pmHistory = QtWidgets.QDialog()
    ui = Ui_pmHistory()
    ui.setupUi(pmHistory)
    pmHistory.show()
    sys.exit(app.exec_())

