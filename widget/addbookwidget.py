from PySide6.QtWidgets import QWidget, QMessageBox
from lib.share import SI
from widget.ui_addbookwidget import Ui_AddBookWidget
from database.connector import Connector


class AddBookWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AddBookWidget()
        self.__ui.setupUi(self)
        self.__ui.m_returnButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(5))
        self.__ui.m_addButton.clicked.connect(self.addBook)

    def addBook(self):
        name = self.__ui.m_titleLineEdit.text()
        author = self.__ui.m_authorLineEdit.text()
        publish_date = self.__ui.m_publishDateEdit.date()
        publish_name = self.__ui.m_publishLineEdit.text()
        price = self.__ui.m_priceSpinBox.text()
        intro = self.__ui.m_introLineEdit.text()
        publish_date = '{}-{}-{}'.format(publish_date.year(), publish_date.month(), publish_date.day())
        if name == '' or author == '' or publish_name == '' or intro == '':
            QMessageBox.information(self, '添加失败', '请填完全部信息再添加书籍')
            return
        cursor = Connector.get_cursor()
        sql = """
            INSERT INTO book (b_name, author, publish_date, publish_name, price, intro)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(sql, (name, author, publish_date, publish_name, price, intro))
        Connector.get_connection()
        QMessageBox.information(self, '添加成功', '添加书籍成功')
        SI.g_mainWindow.updateAdminWidget()