
# Form implementation generated from reading ui file 'POCT_guii.ui'
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
import sqlite3
import sys
conn = sqlite3.connect('poct.db')
c = conn.cursor()
from table import Ui_MainWindow



class Ui_customization_window(object):
    def tablecode(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            SystemExit




    def setupUi(self, customization_window):
        customization_window.setObjectName("customization_window")
        customization_window.resize(800, 480)
        customization_window.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(customization_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.poct_frame = QtWidgets.QFrame(self.frame)
        self.poct_frame.setGeometry(QtCore.QRect(70, 90, 621, 371))
        self.poct_frame.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid grey;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color:rgb(0,0,0);\n"
"}")
        self.poct_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.poct_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.poct_frame.setObjectName("poct_frame")
        self.patientsname = QtWidgets.QLineEdit(self.poct_frame)
        self.patientsname.setGeometry(QtCore.QRect(130, 80, 351, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(13)
        self.patientsname.setFont(font)
        self.patientsname.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius:20px;\n"
"    color: #ffffff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color:rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(85,170,255);\n"
"    background-color:rgb(43,45,56);\n"
"    }")
        self.patientsname.setText("")
        self.patientsname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.patientsname.setObjectName("patientsname")
        self.Test = QtWidgets.QLineEdit(self.poct_frame)
        self.Test.setGeometry(QtCore.QRect(130, 140, 351, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(13)
        self.Test.setFont(font)
        self.Test.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius:20px;\n"
"    color: #ffffff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color:rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(85,170,255);\n"
"    background-color:rgb(43,45,56);\n"
"    }")

        self.Test.setText("")
        self.Test.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Test.setObjectName("Test")


        self.button_Instructions = QtWidgets.QPushButton(self.poct_frame)
        self.button_Instructions.setGeometry(QtCore.QRect(40, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_Instructions.setFont(font)
        self.button_Instructions.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(44, 62, 80);\n"
"    border-radius:20px;\n"
"    color: #ffffff;\n"
"    background-color:rgb(0,0,0);\n"
"}\n"
"QPushButton{background-color:rgb(0,0,0);\n"
"    color: #FFF;\n"
"\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border:2px solid rgb(85,170,255);\n"
"    background-color:rgb(43,45,56);\n"
"    }\n"
"")
        self.button_Instructions.setObjectName("button_Instructions")
        self.button_PlaceCatridge = QtWidgets.QPushButton(self.poct_frame)
        self.button_PlaceCatridge.setGeometry(QtCore.QRect(410, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_PlaceCatridge.setFont(font)
        self.button_PlaceCatridge.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(44, 62, 80);\n"
"    border-radius:20px;\n"
"    color: #ffffff;\n"
"    background-color:rgb(0,0,0);\n"
"}\n"
"QPushButton{background-color:rgb(0,0,0);\n"
"    color: #FFF;\n"
"\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border:2px solid rgb(255, 53, 53);\n"
"    background-color:rgb(43,45,56);\n"
"    }")
        self.button_PlaceCatridge.setObjectName("button_PlaceCatridge")
        self.button_closecustomizationwindow = QtWidgets.QPushButton(self.frame)
        self.button_closecustomizationwindow.setGeometry(QtCore.QRect(700, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)

        self.button_closecustomizationwindow.setFont(font)
        self.button_closecustomizationwindow.setStyleSheet("QPushButton{background-color:rgb(0,0,0);\n"
"    color: #FFF;\n"
"    border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border:2px solid rgb(85,170,255);\n"
"    background-color:rgb(43,45,56);\n"
"    }\n"
"")
        self.button_closecustomizationwindow.setObjectName("button_closecustomizationwindow")
        self.button_runtest = QtWidgets.QPushButton(self.frame)
        self.button_runtest.setGeometry(QtCore.QRect(380, 500, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_runtest.setFont(font)
        self.button_runtest.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(44, 62, 80);\n"
"    border-radius:20px;\n"
"    color: #ffffff;\n"
"    background-color:rgb(0,0,0);\n"
"}\n"
"QPushButton{background-color:rgb(0,0,0);\n"
"    color: #FFF;\n"
"\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border:2px solid rgb(255, 53, 53);\n"
"    background-color:rgb(43,45,56);\n"
"    }")

        self.button_runtest.setObjectName("button_runtest")
        self.button_runtest.clicked.connect(self.create_table)
        self.verticalLayout.addWidget(self.frame)
        customization_window.setCentralWidget(self.centralwidget)
        self.button_Instructions.clicked.connect(self.tablecode)

        self.retranslateUi(customization_window)
        QtCore.QMetaObject.connectSlotsByName(customization_window)


    def create_table(self):
            global name, test
            name = self.patientsname.text()
            test = self.Test.text()

            c.execute('CREATE TABLE IF NOT EXISTS poct (Name TEXT, Test TEXT)')
            c.execute("INSERT INTO poct (Name, Test) VALUES(?, ?)", (name, test))
            for row in c.execute('SELECT * FROM poct'):
                print(row)

            conn.commit()


    def retranslateUi(self, customization_window):
        _translate = QtCore.QCoreApplication.translate
        customization_window.setWindowTitle(_translate("customization_window", "MainWindow"))
        self.patientsname.setPlaceholderText(_translate("customization_window", "Patient\'s Name"))
        self.Test.setPlaceholderText(_translate("customization_window", "Test"))
        self.button_Instructions.setText(_translate("customization_window", "Instructions"))
        self.button_PlaceCatridge.setText(_translate("customization_window", "Place Catridge"))
        self.button_closecustomizationwindow.setText(_translate("customization_window", "X"))
        self.button_runtest.setText(_translate("customization_window", "Run Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customization_window = QtWidgets.QMainWindow()
    ui = Ui_customization_window()
    ui.setupUi(customization_window)
    customization_window.show()
    sys.exit(app.exec_())
