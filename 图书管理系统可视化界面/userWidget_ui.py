# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 450)
        Widget.setMinimumSize(QSize(800, 450))
        Widget.setMaximumSize(QSize(800, 450))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -50, 501, 131))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.lineEdit_name = QLineEdit(Widget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(260, 110, 381, 51))
        self.lineEdit_name.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 70, 501, 131))
        self.label_2.setFont(font)
        self.lineEdit_password = QLineEdit(Widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(261, 210, 381, 51))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(151, 170, 501, 131))
        self.label_3.setFont(font)
        self.pushButton_login = QPushButton(Widget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(340, 310, 91, 41))
        self.pushButton_login.setFont(font)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u5f53\u524d\u6a21\u5f0f\uff1a\u8bfb\u8005\u6a21\u5f0f", None))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u59d3\u540d\uff1a", None))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u5bc6\u7801\uff1a", None))
        self.pushButton_login.setText(QCoreApplication.translate("Widget", u"\u767b\u5f55", None))
    # retranslateUi

