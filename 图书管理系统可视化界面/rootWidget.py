from PySide2.QtWidgets import QWidget
from rootWidget_ui import Ui_Widget
from adminWidget import adminWidget
from userWidget import userWidget
from lib.share import SI


class rootWidget(QWidget):
    def __init__(self):
        super(rootWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_admin.clicked.connect(self.enterAdmin)
        self.ui.pushButton_user.clicked.connect(self.enterUser)

    def enterAdmin(self):
        self.close()
        SI.adminWidget = adminWidget()
        SI.adminWidget.show()

    def enterUser(self):
        self.close()
        SI.userWidget = userWidget()
        SI.userWidget.show()
