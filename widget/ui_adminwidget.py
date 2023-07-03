# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminwidget.ui'
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

from view.bookinfoviewforadmin import BookInfoViewForAdmin

class Ui_AdminWidget(object):
    def setupUi(self, AdminWidget):
        if not AdminWidget.objectName():
            AdminWidget.setObjectName(u"AdminWidget")
        AdminWidget.resize(631, 464)
        self.verticalLayout = QVBoxLayout(AdminWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_addBookButton = QPushButton(AdminWidget)
        self.m_addBookButton.setObjectName(u"m_addBookButton")

        self.horizontalLayout.addWidget(self.m_addBookButton)

        self.m_logoutButton = QPushButton(AdminWidget)
        self.m_logoutButton.setObjectName(u"m_logoutButton")
        self.m_logoutButton.setStyleSheet(u"background-color: red")

        self.horizontalLayout.addWidget(self.m_logoutButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.m_bookInfoView = BookInfoViewForAdmin(AdminWidget)
        self.m_bookInfoView.setObjectName(u"m_bookInfoView")

        self.verticalLayout.addWidget(self.m_bookInfoView)


        self.retranslateUi(AdminWidget)

        QMetaObject.connectSlotsByName(AdminWidget)
    # setupUi

    def retranslateUi(self, AdminWidget):
        AdminWidget.setWindowTitle(QCoreApplication.translate("AdminWidget", u"Form", None))
        self.m_addBookButton.setText(QCoreApplication.translate("AdminWidget", u"\u6dfb\u52a0\u4e66\u7c4d", None))
        self.m_logoutButton.setText(QCoreApplication.translate("AdminWidget", u"\u9000\u51fa\u767b\u5f55", None))
    # retranslateUi

