# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

import results

conn = psycopg2.connect(dbname='dev_db',
                        user='postgres',
                        port=5432,
                        password='post56GRes12',
                        host='localhost')
conn.autocommit = True


class JudgeWindow(QMainWindow):
    def __init__(self, role):
        super(QMainWindow, self).__init__()
        self.setObjectName("window_sudia")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setStyleSheet("background-color: rgb(221, 255, 216);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_uspexSudia = QtWidgets.QLabel(self.centralwidget)
        self.label_uspexSudia.setGeometry(QtCore.QRect(80, 40, 480, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_uspexSudia.setFont(font)
        self.label_uspexSudia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uspexSudia.setObjectName("label_uspexSudia")
        self.label_punktSudia = QtWidgets.QLabel(self.centralwidget)
        self.label_punktSudia.setGeometry(QtCore.QRect(200, 100, 240, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_punktSudia.setFont(font)
        self.label_punktSudia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_punktSudia.setObjectName("label_punktSudia")
        self.pushButton_viewInformationSud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viewInformationSud.setGeometry(QtCore.QRect(40, 160, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_viewInformationSud.setFont(font)
        self.pushButton_viewInformationSud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_viewInformationSud.setStyleSheet("QPushButton{\n"
                                                         "    border: 3px solid  rgb(183, 181, 185);\n"
                                                         "    border-radius: 10px;\n"
                                                         "    background-color: rgb(156, 255, 153);\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "   background-color: rgb(228, 255, 241);\n"
                                                         "}")
        self.pushButton_viewInformationSud.setObjectName("pushButton_viewInformationSud")
        self.pushButton_viewInformationSud.clicked.connect(self.view_results)
        self.pushButton_changeResultsSud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeResultsSud.setGeometry(QtCore.QRect(330, 160, 275, 70))
        self.pushButton_changeResultsSud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeResultsSud.setStyleSheet("QPushButton{\n"
                                                       "    border: 3px solid  rgb(183, 181, 185);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: rgb(156, 255, 153);\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "   background-color: rgb(228, 255, 241);\n"
                                                       "}")
        self.pushButton_changeResultsSud.setObjectName("pushButton_changeResultsSud")
        self.pushButton_changeAdressSud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeAdressSud.setGeometry(QtCore.QRect(40, 250, 275, 70))
        self.pushButton_changeAdressSud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeAdressSud.setStyleSheet("QPushButton{\n"
                                                      "    border: 3px solid  rgb(183, 181, 185);\n"
                                                      "    border-radius: 10px;\n"
                                                      "    background-color: rgb(156, 255, 153);\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "   background-color: rgb(228, 255, 241);\n"
                                                      "}")
        self.pushButton_changeAdressSud.setObjectName("pushButton_changeAdressSud")
        self.pushButton_changeGraphicSorevSud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeGraphicSorevSud.setGeometry(QtCore.QRect(330, 250, 275, 70))
        self.pushButton_changeGraphicSorevSud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeGraphicSorevSud.setStyleSheet("QPushButton{\n"
                                                            "    border: 3px solid  rgb(183, 181, 185);\n"
                                                            "    border-radius: 10px;\n"
                                                            "    background-color: rgb(156, 255, 153);\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "   background-color: rgb(228, 255, 241);\n"
                                                            "}")
        self.pushButton_changeGraphicSorevSud.setObjectName("pushButton_changeGraphicSorevSud")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, window_sudia):
        _translate = QtCore.QCoreApplication.translate
        window_sudia.setWindowTitle(_translate("window_sudia", "window_sudia"))
        self.label_uspexSudia.setText(_translate("window_sudia", "Вы успешно зашли на сайт! Ваша роль - Судья."))
        self.label_punktSudia.setText(_translate("window_sudia", "Выберите нужный пункт:"))
        self.pushButton_viewInformationSud.setText(_translate("window_sudia", "Посмотреть результаты"))
        self.pushButton_changeResultsSud.setText(_translate("window_sudia", "Редактировать результаты"))
        self.pushButton_changeAdressSud.setText(_translate("window_sudia", "Редактировать адрес"))
        self.pushButton_changeGraphicSorevSud.setText(_translate("window_sudia", "Редактировать график соревнований"))

    def view_results(self):
        try:
            df = pd.read_sql('''
                                SELECT g.название_соревнования as "Соревнования", u.фи as "Имя", t.фио as "Тренер", 
                                        k.название_клуба as "Клуб", p.название_программы as "Программа", 
                                        s.название_разряда as "Разряд", r.сумма_баллов as "Сумма баллов", 
                                        r.место as "Место"
                                FROM Результаты as r INNER JOIN График_соревнований as g 
                                        ON r.код_соревнований = g.код_соревнований
                                        INNER JOIN Участники as u ON r.код_участника = u.код_участника
                                        INNER JOIN Тренеры as t ON r.код_тренера = t.код_тренера
                                        INNER JOIN Спортивные_разряды as s ON r.код_разряда = s.код_разряда
                                        INNER JOIN Программы as p  ON r.код_программы = p.код_программы
                                        INNER JOIN Клубы as k ON r.код_клуба = k.код_клуба
                            ''', conn)
            headers = df.columns.values.tolist()
            self.mainWindow = results.ResultWindow(headers, df)

        except psycopg2.DatabaseError as error:
            print("Error: ", error)
        else:
            conn.commit()
