# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userCreatWidget.ui'
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
        self.lineEdit_tele = QLineEdit(Widget)
        self.lineEdit_tele.setObjectName(u"lineEdit_tele")
        self.lineEdit_tele.setGeometry(QRect(330, 111, 201, 20))
        self.lineEdit_name = QLineEdit(Widget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(330, 79, 201, 20))
        self.pushButton_add = QPushButton(Widget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(360, 330, 75, 24))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 142, 71, 20))
        self.lineEdit_balance = QLineEdit(Widget)
        self.lineEdit_balance.setObjectName(u"lineEdit_balance")
        self.lineEdit_balance.setGeometry(QRect(330, 174, 201, 20))
        self.lineEdit_unit = QLineEdit(Widget)
        self.lineEdit_unit.setObjectName(u"lineEdit_unit")
        self.lineEdit_unit.setGeometry(QRect(330, 237, 201, 20))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 174, 71, 20))
        self.lineEdit_password = QLineEdit(Widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(330, 206, 201, 20))
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 206, 71, 20))
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 237, 71, 20))
        self.comboBox_sex = QComboBox(Widget)
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.setObjectName(u"comboBox_sex")
        self.comboBox_sex.setGeometry(QRect(330, 141, 68, 22))
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(229, 268, 71, 20))
        self.comboBox_role = QComboBox(Widget)
        self.comboBox_role.addItem("")
        self.comboBox_role.addItem("")
        self.comboBox_role.addItem("")
        self.comboBox_role.addItem("")
        self.comboBox_role.setObjectName(u"comboBox_role")
        self.comboBox_role.setGeometry(QRect(330, 266, 68, 22))

        self.retranslateUi(Widget)

        self.comboBox_sex.setCurrentIndex(-1)
        self.comboBox_role.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u59d3\u540d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u624b\u673a\u53f7\uff1a", None))
        self.lineEdit_tele.setPlaceholderText("")
        self.lineEdit_name.setPlaceholderText("")
        self.pushButton_add.setText(QCoreApplication.translate("Widget", u"\u65b0\u589e\u8bfb\u8005", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u6027\u522b\uff1a", None))
        self.lineEdit_balance.setPlaceholderText("")
        self.lineEdit_unit.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u4f59\u989d\uff1a", None))
        self.lineEdit_password.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u5bc6\u7801\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u5355\u4f4d\uff1a", None))
        self.comboBox_sex.setItemText(0, QCoreApplication.translate("Widget", u"\u7537", None))
        self.comboBox_sex.setItemText(1, QCoreApplication.translate("Widget", u"\u5973", None))

        self.label_11.setText(QCoreApplication.translate("Widget", u"\u4eba\u5458\u7c7b\u522b\uff1a", None))
        self.comboBox_role.setItemText(0, QCoreApplication.translate("Widget", u"\u6559\u5e08", None))
        self.comboBox_role.setItemText(1, QCoreApplication.translate("Widget", u"\u7814\u7a76\u751f", None))
        self.comboBox_role.setItemText(2, QCoreApplication.translate("Widget", u"\u672c\u79d1\u751f", None))
        self.comboBox_role.setItemText(3, QCoreApplication.translate("Widget", u"\u5176\u4ed6", None))

    # retranslateUi

