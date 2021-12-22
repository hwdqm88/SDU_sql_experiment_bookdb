# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookEditWidget.ui'
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
        self.label_4.setGeometry(QRect(230, 79, 71, 20))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 111, 71, 20))
        self.lineEdit_author = QLineEdit(Widget)
        self.lineEdit_author.setObjectName(u"lineEdit_author")
        self.lineEdit_author.setGeometry(QRect(330, 111, 201, 20))
        self.lineEdit_name = QLineEdit(Widget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(330, 79, 201, 20))
        self.pushButton_delete = QPushButton(Widget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(493, 38, 75, 24))
        self.pushButton_edit = QPushButton(Widget)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setGeometry(QRect(366, 38, 75, 24))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 40, 84, 16))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 142, 71, 20))
        self.lineEdit_publish = QLineEdit(Widget)
        self.lineEdit_publish.setObjectName(u"lineEdit_publish")
        self.lineEdit_publish.setGeometry(QRect(330, 174, 201, 20))
        self.lineEdit_intro = QLineEdit(Widget)
        self.lineEdit_intro.setObjectName(u"lineEdit_intro")
        self.lineEdit_intro.setGeometry(QRect(330, 237, 201, 20))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 174, 71, 20))
        self.lineEdit_price = QLineEdit(Widget)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setGeometry(QRect(330, 206, 201, 20))
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 206, 71, 20))
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 237, 71, 20))
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(229, 268, 71, 20))
        self.comboBox_borrowed = QComboBox(Widget)
        self.comboBox_borrowed.addItem("")
        self.comboBox_borrowed.addItem("")
        self.comboBox_borrowed.setObjectName(u"comboBox_borrowed")
        self.comboBox_borrowed.setGeometry(QRect(330, 266, 68, 22))
        self.lineEdit_date = QLineEdit(Widget)
        self.lineEdit_date.setObjectName(u"lineEdit_date")
        self.lineEdit_date.setGeometry(QRect(330, 141, 201, 20))

        self.retranslateUi(Widget)

        self.comboBox_borrowed.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u4e66\u540d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u4f5c\u8005\uff1a", None))
        self.lineEdit_author.setPlaceholderText("")
        self.lineEdit_name.setPlaceholderText("")
        self.pushButton_delete.setText(QCoreApplication.translate("Widget", u"\u5220\u9664\u56fe\u4e66", None))
        self.pushButton_edit.setText(QCoreApplication.translate("Widget", u"\u4fee\u6539\u4fe1\u606f", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u56fe\u4e66\u7ba1\u7406\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u51fa\u7248\u65e5\u671f\uff1a", None))
        self.lineEdit_publish.setPlaceholderText("")
        self.lineEdit_intro.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u51fa\u7248\u793e\uff1a", None))
        self.lineEdit_price.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u4ef7\u683c\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u7b80\u4ecb\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u662f\u5426\u501f\u51fa\uff1a", None))
        self.comboBox_borrowed.setItemText(0, QCoreApplication.translate("Widget", u"\u5426", None))
        self.comboBox_borrowed.setItemText(1, QCoreApplication.translate("Widget", u"\u662f", None))

        self.lineEdit_date.setPlaceholderText("")
    # retranslateUi

