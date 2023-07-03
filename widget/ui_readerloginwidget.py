# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'readerloginwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ReaderLoginWidget(object):
    def setupUi(self, ReaderLoginWidget):
        if not ReaderLoginWidget.objectName():
            ReaderLoginWidget.setObjectName(u"ReaderLoginWidget")
        ReaderLoginWidget.resize(591, 456)
        self.verticalLayout = QVBoxLayout(ReaderLoginWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(ReaderLoginWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(ReaderLoginWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.m_accountLineEdit = QLineEdit(ReaderLoginWidget)
        self.m_accountLineEdit.setObjectName(u"m_accountLineEdit")

        self.horizontalLayout.addWidget(self.m_accountLineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(ReaderLoginWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.m_passwordLineEdit = QLineEdit(ReaderLoginWidget)
        self.m_passwordLineEdit.setObjectName(u"m_passwordLineEdit")
        self.m_passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.m_passwordLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.m_loginButton = QPushButton(ReaderLoginWidget)
        self.m_loginButton.setObjectName(u"m_loginButton")

        self.horizontalLayout_3.addWidget(self.m_loginButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.m_registerButton = QPushButton(ReaderLoginWidget)
        self.m_registerButton.setObjectName(u"m_registerButton")

        self.horizontalLayout_3.addWidget(self.m_registerButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.m_returnButton = QPushButton(ReaderLoginWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")

        self.horizontalLayout_3.addWidget(self.m_returnButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ReaderLoginWidget)

        QMetaObject.connectSlotsByName(ReaderLoginWidget)
    # setupUi

    def retranslateUi(self, ReaderLoginWidget):
        ReaderLoginWidget.setWindowTitle(QCoreApplication.translate("ReaderLoginWidget", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u8bfb\u8005\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u59d3\u540d\uff1a", None))
        self.m_accountLineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u5bc6\u7801\uff1a", None))
        self.m_passwordLineEdit.setText("")
        self.m_loginButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u767b\u5f55", None))
        self.m_registerButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u6ce8\u518c", None))
        self.m_returnButton.setText(QCoreApplication.translate("ReaderLoginWidget", u"\u8fd4\u56de", None))
    # retranslateUi

