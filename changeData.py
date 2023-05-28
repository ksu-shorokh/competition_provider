from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow


class ChangeDataWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setObjectName("change_data")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setStyleSheet("background-color: rgb(221, 255, 216);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_change_data = QtWidgets.QLabel(self.centralwidget)
        self.label_change_data.setGeometry(QtCore.QRect(10, 100, 620, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_change_data.setFont(font)
        self.label_change_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_change_data.setObjectName("label_change_data")

        self.lineEdit_object = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_object.setGeometry(QtCore.QRect(50, 130, 540, 30))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lineEdit_object.setFont(font)
        self.lineEdit_object.setStyleSheet("border: 3px solid  rgb(183, 181, 185);\n"
                                           "border-radius: 10px;\n"
                                           "")
        self.lineEdit_object.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_object.setObjectName("lineEdit_object")

        self.lineEdit_new = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new.setGeometry(QtCore.QRect(50, 230, 540, 30))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lineEdit_new.setFont(font)
        self.lineEdit_new.setStyleSheet("border: 3px solid  rgb(183, 181, 185);\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.lineEdit_new.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_new.setObjectName("lineEdit_new")

        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setGeometry(QtCore.QRect(100, 320, 440, 40))
        self.pushButton_edit.clicked.connect(self.save_data_tr)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.pushButton_edit.setFont(font)
        self.pushButton_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_edit.setStyleSheet("QPushButton{\n"
                                           "    border: 3px solid  rgb(183, 181, 185);\n"
                                           "    border-radius: 10px;\n"
                                           "    background-color: rgb(183, 181, 185);\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: rgb(211, 208, 213);\n"
                                           "}")
        self.pushButton_edit.setObjectName("pushButton_enter")

        self.setCentralWidget(self.centralwidget)
        self.retranslate(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate(self, change_data):
        _translate = QtCore.QCoreApplication.translate
        change_data.setWindowTitle(_translate("change_data", "Изменить данные"))
        self.label_change_data.setText(_translate("change_data", "Что хотите изменить (ФИО, дата рождения, статус)?"))
        self.pushButton_edit.setText(_translate("change_data", "Изменить"))

    def save_data_tr(self):
        column = self.lineEdit_object.text()
        data_edit = self.lineEdit_new.text()
        return column, data_edit
