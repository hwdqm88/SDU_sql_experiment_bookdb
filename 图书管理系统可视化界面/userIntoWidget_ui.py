# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userIntoWidget.ui'
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
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 71, 20))
        self.lineEdit_name = QLineEdit(Widget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setEnabled(False)
        self.lineEdit_name.setGeometry(QRect(130, 150, 201, 20))
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 214, 71, 20))
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 245, 71, 20))
        self.lineEdit_unit = QLineEdit(Widget)
        self.lineEdit_unit.setObjectName(u"lineEdit_unit")
        self.lineEdit_unit.setGeometry(QRect(130, 245, 201, 20))
        self.pushButton_edit = QPushButton(Widget)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(142, 108, 75, 24))
        self.pushButton_delete = QPushButton(Widget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(254, 108, 75, 24))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 182, 71, 20))
        self.lineEdit_password = QLineEdit(Widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(130, 214, 201, 20))
        self.lineEdit_tele = QLineEdit(Widget)
        self.lineEdit_tele.setObjectName(u"lineEdit_tele")
        self.lineEdit_tele.setGeometry(QRect(130, 182, 201, 20))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 110, 84, 16))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(436, 152, 84, 16))
        self.lineEdit_book_name = QLineEdit(Widget)
        self.lineEdit_book_name.setObjectName(u"lineEdit_book_name")
        self.lineEdit_book_name.setGeometry(QRect(535, 191, 201, 20))
        self.lineEdit_book_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(435, 191, 71, 20))
        self.pushButton_book_find = QPushButton(Widget)
        self.pushButton_book_find.setObjectName(u"pushButton_book_find")
        self.pushButton_book_find.setGeometry(QRect(610, 150, 75, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u59d3\u540d\uff1a", None))
        self.lineEdit_name.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u5bc6\u7801\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u5355\u4f4d\uff1a", None))
        self.lineEdit_unit.setPlaceholderText("")
        self.pushButton_edit.setText(QCoreApplication.translate("Widget", u"\u4fee\u6539\u4fe1\u606f", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Widget", u"\u5220\u9664\u8d26\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u624b\u673a\u53f7\uff1a", None))
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_tele.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u8d26\u53f7\u7ba1\u7406\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u56fe\u4e66\u501f\u9605\uff1a", None))
        self.lineEdit_book_name.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u4e66\u540d\uff1a", None))
        self.pushButton_book_find.setText(QCoreApplication.translate("Widget", u"\u67e5\u627e\u56fe\u4e66", None))
    # retranslateUi

