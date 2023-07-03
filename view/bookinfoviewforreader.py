from PySide6.QtWidgets import QTableView, QPushButton, QMessageBox, QHeaderView

from lib.share import SI
from database.connector import Connector
from model.bookinfomodel import BookInfoModel


class BookInfoViewForReader(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalHeader().setVisible(False)
        self.__model = BookInfoModel.getInstance()
        self.setModel(self.__model)
        self.__model.update()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # self.setSortingEnabled(True)
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)

    def borrow(self):
        row_index = int(self.sender().whatsThis())
        b_id = self.__model.index(row_index, 5).data()
        cursor = Connector.get_cursor()
        if self.__model.index(row_index, 4).data() == '否':
            if int(SI.g_userInfoModel.index(0, 3).data()) >= int(SI.g_userInfoModel.index(0, 4).data()):
                QMessageBox.information(self, '借阅失败', '已达到最大借阅数量')
                return
            sql = 'UPDATE book SET borrowed = 1 WHERE b_id = %s;'
            cursor.execute(sql, b_id)
            Connector.get_connection()
            sql = 'INSERT INTO borrow VALUES (%s, %s);'
            cursor = Connector.get_cursor()
            cursor.execute(sql, (b_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '借阅成功', '借阅成功')
        else:
            sql = 'SELECT * FROM borrow WHERE u_id = %s AND b_id = %s;'
            cursor.execute(sql, (SI.g_userId, b_id))
            if cursor.fetchone() is None:
                QMessageBox.information(self, '归还失败', '这本书是别人借阅的')
                return
            sql = 'UPDATE `book` SET borrowed = 0 WHERE b_id = %s;'
            cursor.execute(sql, b_id)
            Connector.get_connection()
            cursor = Connector.get_cursor()
            sql = 'DELETE FROM `borrow` WHERE b_id = %s AND u_id = %s;'
            cursor.execute(sql, (b_id, SI.g_userId))
            Connector.get_connection()
            QMessageBox.information(self, '归还成功', '归还成功')
        self.updateData()
        SI.g_userInfoModel.update()

    def updateData(self):
        self.__model.update()
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('借阅/归还')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.borrow)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)
