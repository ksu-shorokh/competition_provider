# -*- coding: utf-8 -*-
import psycopg2
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow

import changeData
import dataTr
import results

conn = psycopg2.connect(dbname='dev_db',
                        user='postgres',
                        port=5432,
                        password='post56GRes12',
                        host='localhost')
conn.autocommit = True


class CoachWindow(QMainWindow):
    def __init__(self, role):
        super(QMainWindow, self).__init__()
        self.setObjectName("window_trainer")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setStyleSheet("background-color: rgb(221, 255, 216);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_changeDataUchastnikov = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeDataUchastnikov.setGeometry(QtCore.QRect(330, 160, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_changeDataUchastnikov.setFont(font)
        self.pushButton_changeDataUchastnikov.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeDataUchastnikov.setStyleSheet("QPushButton{\n"
                                                            "    border: 3px solid  rgb(183, 181, 185);\n"
                                                            "    border-radius: 10px;\n"
                                                            "    background-color: rgb(156, 255, 153);\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "   background-color: rgb(228, 255, 241);\n"
                                                            "}")
        self.pushButton_changeDataUchastnikov.setObjectName("pushButton_changeDataUchastnikov")
        self.pushButton_viewInformationTr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viewInformationTr.setGeometry(QtCore.QRect(40, 160, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_viewInformationTr.setFont(font)
        self.pushButton_viewInformationTr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_viewInformationTr.setStyleSheet("QPushButton{\n"
                                                        "    border: 3px solid  rgb(183, 181, 185);\n"
                                                        "    border-radius: 10px;\n"
                                                        "    background-color: rgb(156, 255, 153);\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "   background-color: rgb(228, 255, 241);\n"
                                                        "}")
        self.pushButton_viewInformationTr.setObjectName("pushButton_viewInformationTr")
        self.pushButton_viewInformationTr.clicked.connect(self.view_results)
        self.pushButton_changeDataSvoiTr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeDataSvoiTr.setGeometry(QtCore.QRect(40, 250, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_changeDataSvoiTr.setFont(font)
        self.pushButton_changeDataSvoiTr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeDataSvoiTr.setStyleSheet("QPushButton{\n"
                                                       "    border: 3px solid  rgb(183, 181, 185);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: rgb(156, 255, 153);\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "   background-color: rgb(228, 255, 241);\n"
                                                       "}")
        self.pushButton_changeDataSvoiTr.setObjectName("pushButton_changeDataSvoiTr")
        self.pushButton_changeDataSvoiTr.clicked.connect(self.change_data_coach)
        self.label_uspexTrainer = QtWidgets.QLabel(self.centralwidget)
        self.label_uspexTrainer.setGeometry(QtCore.QRect(20, 40, 600, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_uspexTrainer.setFont(font)
        self.label_uspexTrainer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uspexTrainer.setObjectName("label_uspexTrainer")
        self.label_uspexTrainer.setText("Вы успешно авторизовались на сайте! Ваша роль - {}. ".format(role))
        self.label_punktTrainer = QtWidgets.QLabel(self.centralwidget)
        self.label_punktTrainer.setGeometry(QtCore.QRect(200, 100, 240, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        font.setPointSize(16)
        self.label_punktTrainer.setFont(font)
        self.label_punktTrainer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_punktTrainer.setObjectName("label_punktTrainer")
        self.pushButton_changeDataClubTr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changeDataClubTr.setGeometry(QtCore.QRect(330, 250, 275, 70))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFontMonospaced")
        self.pushButton_changeDataClubTr.setFont(font)
        self.pushButton_changeDataClubTr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeDataClubTr.setStyleSheet("QPushButton{\n"
                                                       "    border: 3px solid  rgb(183, 181, 185);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: rgb(156, 255, 153);\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "   background-color: rgb(228, 255, 241);\n"
                                                       "}")
        self.pushButton_changeDataClubTr.setObjectName("pushButton_changeDataClubTr")
        self.setCentralWidget(self.centralwidget)

        self.retranslate(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate(self, window_trainer):
        _translate = QtCore.QCoreApplication.translate
        window_trainer.setWindowTitle(_translate("window_trainer", "window_trainer"))
        self.pushButton_changeDataUchastnikov.setText(_translate("window_trainer", "Редактировать данные участников"))
        self.pushButton_viewInformationTr.setText(_translate("window_trainer", "Посмотреть результаты"))
        self.pushButton_changeDataSvoiTr.setText(_translate("window_trainer", "Редактировать свои данные"))
        self.label_punktTrainer.setText(_translate("window_trainer", "Выберите нужный пункт:"))
        self.pushButton_changeDataClubTr.setText(_translate("window_trainer", "Редактировать данные клуба"))

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

    def change_data_coach(self):
        self.mainWindow = changeData.ChangeDataWindow()
        self.mainWindow.show()
        column, data_edit = self.mainWindow.save_data_tr()
        print(column, data_edit)
        try:
            df = pd.read_sql(f"EXECUTE ChangeDataTr @name = {column}, @data = {data_edit}", conn)
            headers = df.columns.values.tolist()
            self.mainWindow = dataTr.DataTr(headers, df)

        except psycopg2.DatabaseError as error:
            print("Error: ", error)
        else:
            conn.commit()
