# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

import dataUch
import results

conn = psycopg2.connect(dbname='dev_db',
                        user='postgres',
                        port=5432,
                        password='post56GRes12',
                        host='localhost')
conn.autocommit = True


class ParticipantWindow(QMainWindow):
    def __init__(self, role):
        super(QMainWindow, self).__init__()
        self.setObjectName("window_uchastnik")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 484))
        self.setStyleSheet("background-color: rgb(221, 255, 216);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_uspexUchastnik = QtWidgets.QLabel(self.centralwidget)
        self.label_uspexUchastnik.setGeometry(QtCore.QRect(80, 40, 480, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_uspexUchastnik.setFont(font)
        self.label_uspexUchastnik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uspexUchastnik.setObjectName("label_uspexUchastnik")
        self.label_punctUchastnik = QtWidgets.QLabel(self.centralwidget)
        self.label_punctUchastnik.setGeometry(QtCore.QRect(200, 100, 240, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_punctUchastnik.setFont(font)
        self.label_punctUchastnik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_punctUchastnik.setObjectName("label_punctUchastnik")
        self.pushButton_viewDataSvoiUch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viewDataSvoiUch.setGeometry(QtCore.QRect(40, 160, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_viewDataSvoiUch.setFont(font)
        self.pushButton_viewDataSvoiUch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_viewDataSvoiUch.setStyleSheet("QPushButton{\n"
                                                      "    border: 3px solid  rgb(183, 181, 185);\n"
                                                      "    border-radius: 10px;\n"
                                                      "    background-color: rgb(156, 255, 153);\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "   background-color: rgb(228, 255, 241);\n"
                                                      "}")
        self.pushButton_viewDataSvoiUch.setObjectName("pushButton_viewDataSvoiUch")
        self.pushButton_viewDataSvoiUch.clicked.connect(self.view_data_uch)
        self.pushButton_progressUch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_progressUch.setGeometry(QtCore.QRect(330, 160, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_progressUch.setFont(font)
        self.pushButton_progressUch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_progressUch.setStyleSheet("QPushButton{\n"
                                                  "    border: 3px solid  rgb(183, 181, 185);\n"
                                                  "    border-radius: 10px;\n"
                                                  "    background-color: rgb(156, 255, 153);\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "   background-color: rgb(228, 255, 241);\n"
                                                  "}")
        self.pushButton_progressUch.setObjectName("pushButton_progressUch")
        self.pushButton_viewResultsSorev = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viewResultsSorev.setGeometry(QtCore.QRect(175, 250, 295, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_viewResultsSorev.setFont(font)
        self.pushButton_viewResultsSorev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_viewResultsSorev.setStyleSheet("QPushButton{\n"
                                                       "    border: 3px solid  rgb(183, 181, 185);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: rgb(156, 255, 153);\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "   background-color: rgb(228, 255, 241);\n"
                                                       "}")
        self.pushButton_viewResultsSorev.setObjectName("pushButton_viewResultsSorev")
        self.pushButton_viewResultsSorev.clicked.connect(self.view_results)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, window_uchastnik):
        _translate = QtCore.QCoreApplication.translate
        window_uchastnik.setWindowTitle(_translate("window_uchastnik", "window_uchastnik"))
        self.label_uspexUchastnik.setText(
            _translate("window_uchastnik", "Вы успешно зашли на сайт! Ваша роль - Участник."))
        self.label_punctUchastnik.setText(_translate("window_uchastnik", "Выберите нужный пункт:"))
        self.pushButton_viewDataSvoiUch.setText(_translate("window_uchastnik", "Посмотреть данные участников"))
        self.pushButton_progressUch.setText(_translate("window_uchastnik", "Прогресс"))
        self.pushButton_viewResultsSorev.setText(_translate("window_uchastnik", "Посмотреть результаты соревнований"))

    def view_results(self):
        try:
            df_results = pd.read_sql('''
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
            headers = df_results.columns.values.tolist()
            self.mainWindow = results.ResultWindow(headers, df_results)

        except psycopg2.DatabaseError as error:
            print("Error: ", error)
        else:
            conn.commit()

    def view_data_uch(self):
        try:
            df_data_uch = pd.read_sql('''
                                SELECT фи as "Имя", дата_рождения as "Дата рождения", статус as "Статус" 
                                FROM Участники
                            ''', conn)
            headers = df_data_uch.columns.values.tolist()
            self.mainWindow = dataUch.DataUchWindow(headers, df_data_uch)

        except psycopg2.DatabaseError as error:
            print("Error: ", error)
        else:
            conn.commit()
