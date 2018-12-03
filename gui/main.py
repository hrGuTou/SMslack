"""
        SMslack project created by on9 group

        Group members: Haoran He
                       YanFeng Lin
                       QiZhi Zhao

        Course: CSC 336 Database

        This project used MYSQL database and Twilio sms API to build
        a platform mainly for event organizers to send out
        notifications and announcements via SMS.

        Backend sms receiver/listener using Flask and ngrok to expose localhost
        then used it in Twilio sms webhook (POST requests).

        Frontend used PYQT5 to create GUI

        Database used MySQL

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../gui')

from control import *

from announce import Ui_Announce
from explode import Ui_Explode
from gMessage import Ui_gMessage
from pMessage import Ui_pMessage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.endEvent = QtWidgets.QPushButton(self.centralwidget)
        self.endEvent.setObjectName("endEvent")

        self.gridLayout.addWidget(self.endEvent, 3, 0, 1, 1)
        self.announcement = QtWidgets.QPushButton(self.centralwidget)
        self.announcement.setObjectName("announcement")
        self.gridLayout.addWidget(self.announcement, 3, 1, 1, 1)
        self.gMessage = QtWidgets.QPushButton(self.centralwidget)
        self.gMessage.setObjectName("gMessage")
        self.gridLayout.addWidget(self.gMessage, 3, 2, 1, 1)
        self.pMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pMessage.setObjectName("pMessage")
        self.gridLayout.addWidget(self.pMessage, 3, 3, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setObjectName("refresh")
        self.gridLayout.addWidget(self.refresh, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        # self.endEvent.clicked.connect(self.explode)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # UI 连接
        self.refresh.clicked.connect(self.clickedRefresh)
        self.announcement.clicked.connect(self.clickedAnnounce)
        self.endEvent.clicked.connect(self.clickedEnd)
        self.pMessage.clicked.connect(self.clickedpMessage)
        self.gMessage.clicked.connect(self.clickedgMessage)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smslack"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Team Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Project Name"))
        self.endEvent.setText(_translate("MainWindow", "End Event"))
        self.announcement.setText(_translate("MainWindow", "Announcement"))
        self.gMessage.setText(_translate("MainWindow", "Group Message"))
        self.pMessage.setText(_translate("MainWindow", "Personal Message"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))


    def clickedRefresh(self):
        #print("hit")

        try:
            #self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            result = listAllParticipant()

            for i in range(len(result)):
                numRows = self.tableWidget.rowCount()
                self.tableWidget.insertRow(numRows)
                for j in range(len(result[i])):
                    self.tableWidget.setItem(numRows, j, QtWidgets.QTableWidgetItem(result[i][j]))
        except Exception as e:
            print(e)

    def clickedAnnounce(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Announce()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def clickedEnd(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Explode()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def clickedgMessage(self):
        """
            Send Group Message
        """
        gMessage = QtWidgets.QDialog()
        ui = Ui_gMessage()
        ui.setupUi(gMessage)
        gMessage.show()
        gMessage.exec_()

    def clickedpMessage(self):
        """
            Send Private/Personal Message
        """

        pMessage = QtWidgets.QDialog()
        ui = Ui_pMessage()
        ui.setupUi(pMessage)
        pMessage.show()
        pMessage.exec_()
    
    
    

def pyqt_function():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start() #BE
    pyqt_function() #UI

