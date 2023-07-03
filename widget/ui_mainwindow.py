# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from widget.addbookwidget import AddBookWidget
from widget.administerloginwidget import AdministerLoginWidget
from widget.adminwidget import AdminWidget
from widget.borrowwidget import BorrowWidget
from widget.readerloginwidget import ReaderLoginWidget
from widget.registerwidget import RegisterWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 451)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(64, 158, 255);\n"
"    color: white;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    min-width: 70px;\n"
"    max-width: 70px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(102, 177, 255);\n"
"}\n"
"\n"
"#m_welcomeWidget {\n"
"    background-color: white;\n"
"}")
        self.m_welcomeWidget = QWidget()
        self.m_welcomeWidget.setObjectName(u"m_welcomeWidget")
        self.verticalLayout = QVBoxLayout(self.m_welcomeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.m_welcomeWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.m_readerLoginButton = QPushButton(self.m_welcomeWidget)
        self.m_readerLoginButton.setObjectName(u"m_readerLoginButton")

        self.horizontalLayout.addWidget(self.m_readerLoginButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_administerLoginButton = QPushButton(self.m_welcomeWidget)
        self.m_administerLoginButton.setObjectName(u"m_administerLoginButton")

        self.horizontalLayout.addWidget(self.m_administerLoginButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        MainWindow.addWidget(self.m_welcomeWidget)
        self.m_readerLoginWidget = ReaderLoginWidget()
        self.m_readerLoginWidget.setObjectName(u"m_readerLoginWidget")
        MainWindow.addWidget(self.m_readerLoginWidget)
        self.m_administerLoginWidget = AdministerLoginWidget()
        self.m_administerLoginWidget.setObjectName(u"m_administerLoginWidget")
        MainWindow.addWidget(self.m_administerLoginWidget)
        self.m_borrowWidget = BorrowWidget()
        self.m_borrowWidget.setObjectName(u"m_borrowWidget")
        MainWindow.addWidget(self.m_borrowWidget)
        self.m_registerWidget = RegisterWidget()
        self.m_registerWidget.setObjectName(u"m_registerWidget")
        MainWindow.addWidget(self.m_registerWidget)
        self.m_adminWidget = AdminWidget()
        self.m_adminWidget.setObjectName(u"m_adminWidget")
        MainWindow.addWidget(self.m_adminWidget)
        self.m_addBookWidget = AddBookWidget()
        self.m_addBookWidget.setObjectName(u"m_addBookWidget")
        MainWindow.addWidget(self.m_addBookWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf", None))
        self.m_readerLoginButton.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u8005\u767b\u5f55", None))
        self.m_administerLoginButton.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
    # retranslateUi

