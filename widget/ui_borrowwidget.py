# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'borrowwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from view.bookinfoviewforreader import BookInfoViewForReader
from view.userinfoview import UserInfoView

class Ui_BorrowWidget(object):
    def setupUi(self, BorrowWidget):
        if not BorrowWidget.objectName():
            BorrowWidget.setObjectName(u"BorrowWidget")
        BorrowWidget.resize(631, 464)
        self.verticalLayout = QVBoxLayout(BorrowWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m_userInfoView = UserInfoView(BorrowWidget)
        self.m_userInfoView.setObjectName(u"m_userInfoView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_userInfoView.sizePolicy().hasHeightForWidth())
        self.m_userInfoView.setSizePolicy(sizePolicy)
        self.m_userInfoView.setMinimumSize(QSize(0, 100))
        self.m_userInfoView.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.m_userInfoView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_logoutButton = QPushButton(BorrowWidget)
        self.m_logoutButton.setObjectName(u"m_logoutButton")
        self.m_logoutButton.setStyleSheet(u"background-color: red; color: white;")

        self.horizontalLayout.addWidget(self.m_logoutButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.m_bookInfoView = BookInfoViewForReader(BorrowWidget)
        self.m_bookInfoView.setObjectName(u"m_bookInfoView")

        self.verticalLayout.addWidget(self.m_bookInfoView)


        self.retranslateUi(BorrowWidget)

        QMetaObject.connectSlotsByName(BorrowWidget)
    # setupUi

    def retranslateUi(self, BorrowWidget):
        BorrowWidget.setWindowTitle(QCoreApplication.translate("BorrowWidget", u"Form", None))
        self.m_logoutButton.setText(QCoreApplication.translate("BorrowWidget", u"\u9000\u51fa\u767b\u5f55", None))
    # retranslateUi

