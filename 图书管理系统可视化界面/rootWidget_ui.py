# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rootWidget.ui'
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
        self.pushButton_admin = QPushButton(Widget)
        self.pushButton_admin.setObjectName(u"pushButton_admin")
        self.pushButton_admin.setGeometry(QRect(210, 300, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_admin.setFont(font)
        self.pushButton_user = QPushButton(Widget)
        self.pushButton_user.setObjectName(u"pushButton_user")
        self.pushButton_user.setGeometry(QRect(440, 300, 131, 41))
        self.pushButton_user.setFont(font)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 30, 501, 131))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 160, 281, 91))
        self.label_2.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf", None))
        self.pushButton_admin.setText(QCoreApplication.translate("Widget", u"\u7ba1\u7406\u5458", None))
        self.pushButton_user.setText(QCoreApplication.translate("Widget", u"\u8bfb\u8005", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u6b22\u8fce\u4f7f\u7528\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u8bf7\u9009\u62e9\u7528\u6237\u7c7b\u578b", None))
    # retranslateUi

