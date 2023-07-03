from PySide6.QtWidgets import QWidget, QMessageBox
from widget.ui_readerloginwidget import Ui_ReaderLoginWidget
from lib.share import SI
from database.connector import Connector


class ReaderLoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_ReaderLoginWidget()
        self.__ui.setupUi(self)
        self.__ui.m_returnButton.clicked.connect(lambda:
                                                 SI.g_mainWindow.setCurrentIndex(0))
        self.__ui.m_loginButton.clicked.connect(self.login)
        self.__ui.m_registerButton.clicked.connect(self.register)

    def login(self):
        cursor = Connector.get_cursor()
        sql = 'SELECT u_id FROM user WHERE u_name = %s AND password = %s'
        cursor.execute(sql, (self.__ui.m_accountLineEdit.text(), self.__ui.m_passwordLineEdit.text()))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.critical(self, '登陆失败', '用户名或密码错误，请重试')
            return
        SI.g_userId = result[0]
        SI.g_mainWindow.setCurrentIndex(3)
        SI.g_mainWindow.updateBorrowWidget()

    def register(self):
        SI.g_mainWindow.setCurrentIndex(4)
