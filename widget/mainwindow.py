from PySide6.QtWidgets import QStackedWidget
from lib.share import SI
from widget.ui_mainwindow import Ui_MainWindow


class MainWindow(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        SI.g_mainWindow = self
        self.__ui.m_readerLoginButton.clicked.connect(lambda:
                                                      self.setCurrentWidget(self.__ui.m_readerLoginWidget))
        self.__ui.m_administerLoginButton.clicked.connect(lambda:
                                                          self.setCurrentWidget(self.__ui.m_administerLoginWidget))

    def updateBorrowWidget(self):
        self.__ui.m_borrowWidget.updateData()

    def updateAdminWidget(self):
        self.__ui.m_adminWidget.updateData()
