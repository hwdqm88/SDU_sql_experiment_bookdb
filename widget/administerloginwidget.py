from PySide6.QtWidgets import QWidget, QMessageBox
from widget.ui_administerloginwidget import Ui_AdministerLoginWidget
from lib.share import SI
from database.connector import Connector


class AdministerLoginWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AdministerLoginWidget()
        self.__ui.setupUi(self)
        self.__ui.m_returnButton.clicked.connect(lambda:
                                                 SI.g_mainWindow.setCurrentIndex(0))
        self.__ui.m_loginButton.clicked.connect(self.login)

    def login(self):
        cursor = Connector.get_cursor()
        sql = 'SELECT * FROM administer WHERE a_name = %s AND password = %s;'
        cursor.execute(sql, (self.__ui.m_accountLineEdit.text(), self.__ui.m_passwordLineEdit.text()))
        if cursor.fetchone is None:
            QMessageBox.critical(self, '登陆失败', '管理员帐号或密码错误，请检查')
            return
        SI.g_mainWindow.setCurrentIndex(5)