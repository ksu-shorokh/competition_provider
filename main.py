# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

import coachWindow
import judgeWindow
import participantWindow


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        self.type_post = "LOG"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 216);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_enter = QtWidgets.QLabel(self.centralwidget)
        self.label_enter.setGeometry(QtCore.QRect(200, 30, 240, 40))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_enter.setFont(font)
        self.label_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enter.setObjectName("label_enter")
        self.label_nickname = QtWidgets.QLabel(self.centralwidget)
        self.label_nickname.setGeometry(QtCore.QRect(50, 90, 120, 40))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(18)
        self.label_nickname.setFont(font)
        self.label_nickname.setObjectName("label_nickname")
        self.lineEdit_nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nickname.setGeometry(QtCore.QRect(50, 130, 540, 30))
        self.lineEdit_nickname.textChanged.connect(self.checkTextLogin)
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lineEdit_nickname.setFont(font)
        self.lineEdit_nickname.setStyleSheet("border: 3px solid  rgb(183, 181, 185);\n"
                                             "border-radius: 10px;\n"
                                             "")
        self.lineEdit_nickname.setMaxLength(16)
        self.lineEdit_nickname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nickname.setPlaceholderText("nickname123")
        self.lineEdit_nickname.setObjectName("lineEdit_nickname")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(50, 190, 120, 40))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(18)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(50, 230, 540, 30))
        self.lineEdit_password.textChanged.connect(self.checkTextPassword)
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("border: 3px solid  rgb(183, 181, 185);\n"
                                             "border-radius: 10px;\n"
                                             "")
        self.lineEdit_password.setMaxLength(12)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setPlaceholderText("12345678")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.checkBox_showPassword = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_showPassword.setGeometry(QtCore.QRect(50, 265, 210, 30))
        self.checkBox_showPassword.stateChanged.connect(self.showHidePassword)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.checkBox_showPassword.setFont(font)
        self.checkBox_showPassword.setText("Показать пароль")
        self.checkBox_showPassword.setObjectName("checkBox_showPassword")
        self.pushButton_enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter.setGeometry(QtCore.QRect(100, 320, 440, 40))
        self.pushButton_enter.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_enter.setStyleSheet("QPushButton{\n"
                                            "    border: 3px solid  rgb(183, 181, 185);\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb(183, 181, 185);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(211, 208, 213);\n"
                                            "}")
        self.pushButton_enter.setObjectName("pushButton_enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        login = self.lineEdit_nickname.text()
        password = self.lineEdit_password.text()
        role = None

        if password == 'coach':
            role = 'Тренер'
        elif password == 'participant':
            role = 'Участник'
        elif password == 'judge':
            role = 'Судья'
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setBaseSize(400, 150)
            error.setText('Неверный пароль')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.setInformativeText('Попробуйте ввести другой пароль')
            error.buttonClicked.connect(self.push_Ok)
            error.exec_()

        self.accept()
        if role is not None:
            authForm.hide()
            if role == 'Тренер':
                self.mainWindow = coachWindow.CoachWindow(role)
            elif role == 'Участник':
                self.mainWindow = participantWindow.ParticipantWindow(role)
            else:
                self.mainWindow = judgeWindow.JudgeWindow(role)
            self.mainWindow.show()

    def push_Ok(self):
        self.lineEdit_password.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.label_enter.setText(_translate("MainWindow", "Вход:"))
        self.label_nickname.setText(_translate("MainWindow", "Никнейм:"))
        self.label_password.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton_enter.setText(_translate("MainWindow", "Войти"))

    def showHidePassword(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def checkTextLogin(self):
        alphabet = "qwertyuiopasdfghjklzxcvbnm_1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        text = self.lineEdit_nickname.text()
        for x in text:
            if x not in alphabet:
                text = text.replace(x, "")
        self.lineEdit_nickname.setText(text)

    def checkTextPassword(self):
        alphabet = "qwertyuiopasdfghjklzxcvbnm_1234567890QWERTYUIOPASDFGHJKLZXCVBNM#-=/\\"
        text = self.lineEdit_password.text()
        for x in text:
            if x not in alphabet:
                text = text.replace(x, "")
        self.lineEdit_password.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    authForm = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(authForm)
    authForm.show()
    sys.exit(app.exec_())
