# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\MSVC\src\display\z_part\beginning.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.beginning_background = QtWidgets.QLabel(self.centralwidget)
        self.beginning_background.setGeometry(QtCore.QRect(1, -6, 1000, 800))
        self.beginning_background.setMouseTracking(False)
        self.beginning_background.setStyleSheet("background-image: url(:/beginning_background/images/beginning_background.jpg);")
        self.beginning_background.setText("")
        self.beginning_background.setObjectName("beginning_background")
        self.clock = QtWidgets.QLabel(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(740, 760, 261, 31))
        self.clock.setStyleSheet("color: rgb(0, 0, 0);")
        self.clock.setObjectName("clock")
        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(730, 720, 271, 41))
        font = QtGui.QFont()
        font.setFamily("HYPixel 9px")
        self.author.setFont(font)
        self.author.setStyleSheet("color: rgb(0, 0, 0);")
        self.author.setObjectName("author")
        self.add_user = QtWidgets.QPushButton(self.centralwidget)
        self.add_user.setGeometry(QtCore.QRect(0, 30, 101, 28))
        font = QtGui.QFont()
        font.setFamily("HYPixel 9px")
        font.setPointSize(13)
        self.add_user.setFont(font)
        self.add_user.setAutoDefault(True)
        self.add_user.setDefault(True)
        self.add_user.setObjectName("add_user")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(740, 630, 261, 91))
        font = QtGui.QFont()
        font.setFamily("HYPixel 9px")
        font.setPointSize(41)
        self.enter.setFont(font)
        self.enter.setStyleSheet("")
        self.enter.setAutoDefault(True)
        self.enter.setDefault(True)
        self.enter.setObjectName("enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clock.setText(_translate("MainWindow", "TextLabel"))
        self.author.setText(_translate("MainWindow", "制作人：马楷恒，张嘉杰，刘杨，朱善哲"))
        self.add_user.setText(_translate("MainWindow", "添加用户"))
        self.enter.setText(_translate("MainWindow", "进入"))
import beginning_background_rc