# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addbookwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddBookWidget(object):
    def setupUi(self, AddBookWidget):
        if not AddBookWidget.objectName():
            AddBookWidget.setObjectName(u"AddBookWidget")
        AddBookWidget.resize(675, 389)
        self.verticalLayout = QVBoxLayout(AddBookWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(AddBookWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)

        self.m_titleLineEdit = QLineEdit(AddBookWidget)
        self.m_titleLineEdit.setObjectName(u"m_titleLineEdit")

        self.horizontalLayout.addWidget(self.m_titleLineEdit)

        self.horizontalSpacer_7 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(AddBookWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.m_authorLineEdit = QLineEdit(AddBookWidget)
        self.m_authorLineEdit.setObjectName(u"m_authorLineEdit")

        self.horizontalLayout_2.addWidget(self.m_authorLineEdit)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(AddBookWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.m_publishDateEdit = QDateEdit(AddBookWidget)
        self.m_publishDateEdit.setObjectName(u"m_publishDateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_publishDateEdit.sizePolicy().hasHeightForWidth())
        self.m_publishDateEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.m_publishDateEdit)

        self.horizontalSpacer_9 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(AddBookWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_18)

        self.m_publishLineEdit = QLineEdit(AddBookWidget)
        self.m_publishLineEdit.setObjectName(u"m_publishLineEdit")

        self.horizontalLayout_4.addWidget(self.m_publishLineEdit)

        self.horizontalSpacer_10 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(AddBookWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_19)

        self.m_priceSpinBox = QDoubleSpinBox(AddBookWidget)
        self.m_priceSpinBox.setObjectName(u"m_priceSpinBox")
        sizePolicy.setHeightForWidth(self.m_priceSpinBox.sizePolicy().hasHeightForWidth())
        self.m_priceSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.m_priceSpinBox)

        self.horizontalSpacer_11 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_6 = QLabel(AddBookWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.m_introLineEdit = QLineEdit(AddBookWidget)
        self.m_introLineEdit.setObjectName(u"m_introLineEdit")

        self.horizontalLayout_6.addWidget(self.m_introLineEdit)

        self.horizontalSpacer_12 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.m_addButton = QPushButton(AddBookWidget)
        self.m_addButton.setObjectName(u"m_addButton")

        self.horizontalLayout_7.addWidget(self.m_addButton)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_21)

        self.m_returnButton = QPushButton(AddBookWidget)
        self.m_returnButton.setObjectName(u"m_returnButton")

        self.horizontalLayout_7.addWidget(self.m_returnButton)

        self.horizontalSpacer_14 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)


        self.retranslateUi(AddBookWidget)

        QMetaObject.connectSlotsByName(AddBookWidget)
    # setupUi

    def retranslateUi(self, AddBookWidget):
        AddBookWidget.setWindowTitle(QCoreApplication.translate("AddBookWidget", u"\u6dfb\u52a0\u65b0\u4e66", None))
        self.label.setText(QCoreApplication.translate("AddBookWidget", u"\u6807\u9898\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("AddBookWidget", u"\u4f5c\u8005\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("AddBookWidget", u"\u51fa\u7248\u65e5\u671f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("AddBookWidget", u"\u51fa\u7248\u793e\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("AddBookWidget", u"\u4ef7\u683c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("AddBookWidget", u"\u7b80\u4ecb\uff1a", None))
        self.m_addButton.setText(QCoreApplication.translate("AddBookWidget", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.m_returnButton.setText(QCoreApplication.translate("AddBookWidget", u"\u8fd4\u56de", None))
    # retranslateUi

