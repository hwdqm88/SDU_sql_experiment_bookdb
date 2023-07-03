from PySide6.QtWidgets import QTableView, QPushButton, QListWidget, QHeaderView
from database.connector import Connector
from model.userinfomodel import UserInfoModel
from lib.share import SI


class UserInfoView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__showBorrowWidget = None
        self.verticalHeader().setVisible(False)
        self.__model = UserInfoModel()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.setModel(self.__model)
        show_button = QPushButton('查看已借阅书籍')
        self.setIndexWidget(self.__model.index(0, 6), show_button)
        show_button.setStyleSheet('min-width: 100px; max-width: 100px;')
        show_button.clicked.connect(self.showBorrow)

    def showBorrow(self):
        cursor = Connector.get_cursor()
        sql = """
            SELECT b_name
            FROM borrow
                JOIN book on book.b_id = borrow.b_id
                JOIN user on user.u_id = borrow.u_id
            WHERE borrow.u_id = %s 
        """
        cursor.execute(sql, SI.g_userId)
        result = cursor.fetchall()
        self.__showBorrowWidget = QListWidget()
        self.__showBorrowWidget.setWindowTitle('借阅书籍目录')
        for item in result:
            self.__showBorrowWidget.addItem(item[0])
        self.__showBorrowWidget.show()

    def updateData(self):
        self.__model.update()
