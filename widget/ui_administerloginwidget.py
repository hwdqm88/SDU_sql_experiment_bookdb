# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'administerloginwidget.ui'
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

class Ui_AdministerLoginWidget(object):
    def setupUi(self, AdministerLoginWidget):
        if not AdministerLoginWidget.objectName():
            AdministerLoginWidget.setObjectName(u"AdministerLoginWidget")
        AdministerLoginWidget.resize(796, 568)
        self.verticalLayout = QVBoxLayout(AdministerLoginWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(AdministerLoginWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(AdministerLoginWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.m_accountLineEdit = QLineEdit(AdministerLoginWidget)
        self.m_accountLineEdit.setObjectName(u"m_accountLineEdit")

        self.horizontalLayout.addWidget(self.m_accountLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(AdministerLoginWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.m_passwordLineEdit = QLineEdit(AdministerLoginWidget)
        self.m_passwordLineEdit.setObjectName(u"m_passwordLineEdit")
        self.m_passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.m_passwordLineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.m_loginButton = QPushButton(AdministerLoginWidget)
        self.m_loginButton.setObjectName(u"m_loginButton")

        self.horizontalLayout_3.addWidget(self.m_loginButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.m_returnButton = QPushButton(AdministerLoginWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")

        self.horizontalLayout_3.addWidget(self.m_returnButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AdministerLoginWidget)

        QMetaObject.connectSlotsByName(AdministerLoginWidget)
    # setupUi

    def retranslateUi(self, AdministerLoginWidget):
        AdministerLoginWidget.setWindowTitle(QCoreApplication.translate("AdministerLoginWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AdministerLoginWidget", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("AdministerLoginWidget", u"\u5e10\u53f7\uff1a", None))
        self.m_accountLineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("AdministerLoginWidget", u"\u5bc6\u7801\uff1a", None))
        self.m_passwordLineEdit.setText("")
        self.m_loginButton.setText(QCoreApplication.translate("AdministerLoginWidget", u"\u767b\u5f55", None))
        self.m_returnButton.setText(QCoreApplication.translate("AdministerLoginWidget", u"\u8fd4\u56de", None))
    # retranslateUi

