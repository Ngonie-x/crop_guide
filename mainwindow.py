# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 1121, 91))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.crop_guide_lbl = QtWidgets.QLabel(self.frame)
        self.crop_guide_lbl.setGeometry(QtCore.QRect(430, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(40)
        self.crop_guide_lbl.setFont(font)
        self.crop_guide_lbl.setObjectName("crop_guide_lbl")
        self.submitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitbtn.setGeometry(QtCore.QRect(190, 510, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submitbtn.setFont(font)
        self.submitbtn.setObjectName("submitbtn")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(530, 170, 491, 221))
        self.picture_label.setObjectName("picture_label")
        self.info_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.info_textEdit.setGeometry(QtCore.QRect(530, 430, 491, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.info_textEdit.setFont(font)
        self.info_textEdit.setObjectName("info_textEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(493, 140, 20, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(230, 170, 201, 261))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.season_combobox = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.season_combobox.setFont(font)
        self.season_combobox.setObjectName("season_combobox")
        self.state_combobox = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.state_combobox.setFont(font)
        self.state_combobox.setObjectName("state_combobox")
        self.budget_lineedit = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.budget_lineedit.setFont(font)
        self.budget_lineedit.setObjectName("budget_lineedit")
        self.acres_lineedit = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acres_lineedit.setFont(font)
        self.acres_lineedit.setObjectName("acres_lineedit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 170, 121, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
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
        self.crop_guide_lbl.setText(_translate("MainWindow", "Crop Guide"))
        self.submitbtn.setText(_translate("MainWindow", "submit"))
        self.picture_label.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Season"))
        self.label_2.setText(_translate("MainWindow", "State"))
        self.label_3.setText(_translate("MainWindow", "Budget"))
        self.label_4.setText(_translate("MainWindow", "Acres"))
