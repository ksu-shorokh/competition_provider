from PyQt5 import QtCore, QtWidgets


from PyQt5.QtWidgets import QMainWindow


class DataUchWindow(QMainWindow):
    def __init__(self, headers, df):
        super(QMainWindow, self).__init__()
        self.table = QtWidgets.QTableWidget()
        self.table.setWindowTitle("Данные")
        self.table.setGeometry(200, 170, 1000, 600)
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 300)
        self.table.setColumnWidth(2, 300)
        self.act(df)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def act(self, df):
        for i, row in df.iterrows():
            # Добавление строки
            self.table.setRowCount(self.table.rowCount() + 1)

            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))

        self.table.show()

    def retranslateUi(self, window_result):
        _translate = QtCore.QCoreApplication.translate
        window_result.setWindowTitle(_translate("window_result", "window_result"))
