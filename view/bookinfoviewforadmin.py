from PySide6.QtWidgets import QTableView, QPushButton, QMessageBox, QHeaderView

from lib.share import SI
from database.connector import Connector
from model.bookinfomodel import BookInfoModel


class BookInfoViewForAdmin(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalHeader().setVisible(False)
        self.__model = BookInfoModel.getInstance()
        self.setModel(self.__model)
        self.__model.update()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # self.setSortingEnabled(True)
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('删除')
            borrow_button.setStyleSheet('background-color: red')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.deleteBook)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)

    def deleteBook(self):
        ret = QMessageBox.question(self, '确认删除', '确认删除这本书吗？')
        if ret != QMessageBox.StandardButton.Yes:
            return
        row_index = int(self.sender().whatsThis())
        b_id = self.__model.index(row_index, 5).data()
        sql = 'DELETE FROM borrow WHERE b_id = %s'
        cursor = Connector.get_cursor()
        cursor.execute(sql, b_id)
        sql = 'DELETE FROM book WHERE b_id = %s'
        cursor.execute(sql, b_id)
        Connector.get_connection()
        QMessageBox.information(self, '删除成功', '删除成功')
        self.updateData()

    def updateData(self):
        self.__model.update()
        for i in range(self.__model.rowCount()):
            borrow_button = QPushButton('删除')
            borrow_button.setStyleSheet('background-color: red')
            borrow_button.setWhatsThis(str(i))
            borrow_button.clicked.connect(self.deleteBook)
            self.setIndexWidget(self.__model.index(i, self.__model.columnCount() - 1), borrow_button)
