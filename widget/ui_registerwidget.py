# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_RegisterWidget(object):
    def setupUi(self, RegisterWidget):
        if not RegisterWidget.objectName():
            RegisterWidget.setObjectName(u"RegisterWidget")
        RegisterWidget.resize(708, 429)
        self.verticalLayout = QVBoxLayout(RegisterWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(RegisterWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)

        self.m_nameLlineEdit = QLineEdit(RegisterWidget)
        self.m_nameLlineEdit.setObjectName(u"m_nameLlineEdit")

        self.horizontalLayout.addWidget(self.m_nameLlineEdit)

        self.horizontalSpacer_14 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(RegisterWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.m_genderComboBox = QComboBox(RegisterWidget)
        self.m_genderComboBox.addItem("")
        self.m_genderComboBox.addItem("")
        self.m_genderComboBox.setObjectName(u"m_genderComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_genderComboBox.sizePolicy().hasHeightForWidth())
        self.m_genderComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.m_genderComboBox)

        self.horizontalSpacer_12 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(RegisterWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.m_mobileLineEdit = QLineEdit(RegisterWidget)
        self.m_mobileLineEdit.setObjectName(u"m_mobileLineEdit")

        self.horizontalLayout_3.addWidget(self.m_mobileLineEdit)

        self.horizontalSpacer_10 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(RegisterWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_18)

        self.m_unitLineEdit = QLineEdit(RegisterWidget)
        self.m_unitLineEdit.setObjectName(u"m_unitLineEdit")

        self.horizontalLayout_4.addWidget(self.m_unitLineEdit)

        self.horizontalSpacer_11 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_5 = QLabel(RegisterWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_19)

        self.m_roleComboBox = QComboBox(RegisterWidget)
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.addItem("")
        self.m_roleComboBox.setObjectName(u"m_roleComboBox")
        sizePolicy.setHeightForWidth(self.m_roleComboBox.sizePolicy().hasHeightForWidth())
        self.m_roleComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.m_roleComboBox)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_6 = QLabel(RegisterWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.m_passwordLineEdit = QLineEdit(RegisterWidget)
        self.m_passwordLineEdit.setObjectName(u"m_passwordLineEdit")
        self.m_passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.m_passwordLineEdit)

        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_7 = QLabel(RegisterWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_21)

        self.m_passwordConfirmLineEdit = QLineEdit(RegisterWidget)
        self.m_passwordConfirmLineEdit.setObjectName(u"m_passwordConfirmLineEdit")
        self.m_passwordConfirmLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.m_passwordConfirmLineEdit)

        self.horizontalSpacer_13 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_22 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.m_registerButton = QPushButton(RegisterWidget)
        self.m_registerButton.setObjectName(u"m_registerButton")

        self.horizontalLayout_8.addWidget(self.m_registerButton)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)

        self.m_returnButton = QPushButton(RegisterWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")

        self.horizontalLayout_8.addWidget(self.m_returnButton)

        self.horizontalSpacer_23 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_23)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(RegisterWidget)

        QMetaObject.connectSlotsByName(RegisterWidget)
    # setupUi

    def retranslateUi(self, RegisterWidget):
        RegisterWidget.setWindowTitle(QCoreApplication.translate("RegisterWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("RegisterWidget", u"\u59d3\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("RegisterWidget", u"\u6027\u522b\uff1a", None))
        self.m_genderComboBox.setItemText(0, QCoreApplication.translate("RegisterWidget", u"\u7537", None))
        self.m_genderComboBox.setItemText(1, QCoreApplication.translate("RegisterWidget", u"\u5973", None))

        self.label_3.setText(QCoreApplication.translate("RegisterWidget", u"\u624b\u673a\u53f7\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("RegisterWidget", u"\u5355\u4f4d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("RegisterWidget", u"\u7c7b\u522b\uff1a", None))
        self.m_roleComboBox.setItemText(0, QCoreApplication.translate("RegisterWidget", u"\u6559\u5e08", None))
        self.m_roleComboBox.setItemText(1, QCoreApplication.translate("RegisterWidget", u"\u7814\u7a76\u751f", None))
        self.m_roleComboBox.setItemText(2, QCoreApplication.translate("RegisterWidget", u"\u672c\u79d1\u751f", None))
        self.m_roleComboBox.setItemText(3, QCoreApplication.translate("RegisterWidget", u"\u5176\u4ed6", None))

        self.label_6.setText(QCoreApplication.translate("RegisterWidget", u"\u5bc6\u7801\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("RegisterWidget", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.m_registerButton.setText(QCoreApplication.translate("RegisterWidget", u"\u6ce8\u518c", None))
        self.m_returnButton.setText(QCoreApplication.translate("RegisterWidget", u"\u8fd4\u56de", None))
    # retranslateUi

