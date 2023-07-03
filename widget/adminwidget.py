from PySide6.QtWidgets import QWidget
from lib.share import SI
from widget.ui_adminwidget import Ui_AdminWidget


class AdminWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_AdminWidget()
        self.__ui.setupUi(self)
        self.__ui.m_addBookButton.clicked.connect(self.addBook)
        self.__ui.m_logoutButton.clicked.connect(lambda: SI.g_mainWindow.setCurrentIndex(0))

    def addBook(self):
        SI.g_mainWindow.setCurrentIndex(6)

    def updateData(self):
        self.__ui.m_bookInfoView.updateData()
