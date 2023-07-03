from PySide6.QtWidgets import QWidget
from lib.share import SI
from widget.ui_borrowwidget import Ui_BorrowWidget


class BorrowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_BorrowWidget()
        self.__ui.setupUi(self)
        self.__ui.m_logoutButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(0))

    def updateData(self):
        self.__ui.m_bookInfoView.updateData()
        self.__ui.m_userInfoView.updateData()
