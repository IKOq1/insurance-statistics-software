# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 419)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(217, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 10, 1, 1, 1)

        self.btnAdd = QPushButton(Dialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 10, 0, 1, 1)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.gridLayout.addWidget(self.btnCancel, 10, 2, 1, 1)

        self.lYear = QLineEdit(Dialog)
        self.lYear.setObjectName(u"lYear")

        self.gridLayout.addWidget(self.lYear, 9, 0, 1, 3)

        self.lsCaseCount = QLineEdit(Dialog)
        self.lsCaseCount.setObjectName(u"lsCaseCount")

        self.gridLayout.addWidget(self.lsCaseCount, 7, 0, 1, 3)

        self.lsCount = QLineEdit(Dialog)
        self.lsCount.setObjectName(u"lsCount")

        self.gridLayout.addWidget(self.lsCount, 5, 0, 1, 3)

        self.lObject = QLineEdit(Dialog)
        self.lObject.setObjectName(u"lObject")

        self.gridLayout.addWidget(self.lObject, 3, 0, 1, 3)

        self.cmbTypeS = QComboBox(Dialog)
        self.cmbTypeS.setObjectName(u"cmbTypeS")

        self.gridLayout.addWidget(self.cmbTypeS, 1, 0, 1, 3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 3)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u044b\u0445 \u0441\u043b\u0443\u0447\u0430\u0435\u0432", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u044f ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0434", None))
    # retranslateUi

