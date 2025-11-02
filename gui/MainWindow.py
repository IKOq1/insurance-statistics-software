# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1735, 828)
        MainWindow.setStyleSheet(u"background-color:  #39494d;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow{\n"
"	background-color: #b3ad5b;\n"
"}")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(10, 10, 181, 61))
        font = QFont()
        font.setPointSize(14)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet(u"QPushButton {\n"
"    background-color: gray;  \n"
"    color: white;           \n"
"    border: none;          \n"
"    padding: 8px 16px;         \n"
"    border-radius: 20px;       \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #597d96;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFF8E1;\n"
"}")
        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(200, 10, 111, 61))
        font1 = QFont()
        font1.setPointSize(13)
        self.btnDelete.setFont(font1)
        self.btnDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: #5c6466;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #330c18;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #210405;\n"
"}")
        self.btnChange = QPushButton(self.centralwidget)
        self.btnChange.setObjectName(u"btnChange")
        self.btnChange.setGeometry(QRect(320, 10, 281, 61))
        self.btnChange.setFont(font1)
        self.btnChange.setStyleSheet(u"QPushButton {\n"
"    background-color: gray;  \n"
"    color: white;             \n"
"    border: none;             \n"
"    padding: 8px 16px;         \n"
"    border-radius: 20px;       \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #597d96;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFF8E1;\n"
"}")
        self.cmbObject = QComboBox(self.centralwidget)
        self.cmbObject.setObjectName(u"cmbObject")
        self.cmbObject.setGeometry(QRect(320, 80, 281, 24))
        self.cmbObject.setStyleSheet(u"QComboBox{\n"
"	background-color: #94a2a6;\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"}")
        self.cmbTypeS = QComboBox(self.centralwidget)
        self.cmbTypeS.setObjectName(u"cmbTypeS")
        self.cmbTypeS.setGeometry(QRect(10, 80, 301, 24))
        self.cmbTypeS.setStyleSheet(u"QComboBox{\n"
"	background-color: #94a2a6;\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"}")
        self.btnStartBot = QPushButton(self.centralwidget)
        self.btnStartBot.setObjectName(u"btnStartBot")
        self.btnStartBot.setGeometry(QRect(10, 690, 291, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartBot.sizePolicy().hasHeightForWidth())
        self.btnStartBot.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.btnStartBot.setFont(font2)
        self.btnStartBot.setStyleSheet(u"QPushButton {\n"
"    background-color: gray;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: white;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: none;              /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 */\n"
"    padding: 8px 16px;         /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 */\n"
"    border-radius: 20px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u043c \u0443\u0433\u043b\u044b (10px - \u0440\u0430\u0434\u0438\u0443\u0441) */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QPushButton:pressed {\n"
"    background"
                        "-color: #3d8b40;\n"
"}")
        self.btnUpdateWidget = QPushButton(self.centralwidget)
        self.btnUpdateWidget.setObjectName(u"btnUpdateWidget")
        self.btnUpdateWidget.setGeometry(QRect(310, 690, 291, 71))
        self.btnUpdateWidget.setFont(font1)
        self.btnUpdateWidget.setStyleSheet(u"QPushButton {\n"
"    background-color: gray;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: white;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: none;              /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0443\u044e \u0440\u0430\u043c\u043a\u0443 */\n"
"    padding: 8px 16px;         /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 */\n"
"    border-radius: 20px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u043c \u0443\u0433\u043b\u044b (10px - \u0440\u0430\u0434\u0438\u0443\u0441) */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QPushButton:pressed {\n"
"    background"
                        "-color: #3d8b40;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1380, 20, 331, 411))
        self.label.setPixmap(QPixmap(u"qrL.png"))
        self.label.setScaledContents(True)
        self.chartView1 = QChartView(self.centralwidget)
        self.chartView1.setObjectName(u"chartView1")
        self.chartView1.setGeometry(QRect(610, 450, 691, 321))
        self.chartView1.setStyleSheet(u"QChartView {\n"
"    background-color: transparent;  /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 */\n"
"}")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 430, 591, 251))
        font3 = QFont()
        font3.setPointSize(20)
        self.groupBox.setFont(font3)
        self.lblStatistics = QLabel(self.groupBox)
        self.lblStatistics.setObjectName(u"lblStatistics")
        self.lblStatistics.setGeometry(QRect(10, 30, 571, 211))
        font4 = QFont()
        font4.setPointSize(10)
        self.lblStatistics.setFont(font4)
        self.lblStatistics.setTextFormat(Qt.TextFormat.RichText)
        self.tblView = QTableView(self.centralwidget)
        self.tblView.setObjectName(u"tblView")
        self.tblView.setGeometry(QRect(10, 111, 591, 311))
        self.tblView.setStyleSheet(u"QTableView {\n"
"    background-color: #FFF8E1;  /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0436\u0451\u043b\u0442\u044b\u0439 */\n"
"    alternate-background-color: #2a3136;  /* \u0426\u0432\u0435\u0442 \u0447\u0435\u0440\u0435\u0434\u0443\u044e\u0449\u0438\u0445\u0441\u044f \u0441\u0442\u0440\u043e\u043a */\n"
"	color: #1b2024;\n"
"}")
        self.chartView2 = QChartView(self.centralwidget)
        self.chartView2.setObjectName(u"chartView2")
        self.chartView2.setGeometry(QRect(1300, 450, 421, 321))
        self.chartView2.setStyleSheet(u"QChartView {\n"
"    background-color: transparent;  /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 */\n"
"}")
        self.chartView3 = QChartView(self.centralwidget)
        self.chartView3.setObjectName(u"chartView3")
        self.chartView3.setGeometry(QRect(610, 10, 751, 431))
        self.chartView3.setStyleSheet(u"QChartView {\n"
"    background-color: transparent;  /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 */\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1735, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnChange.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btnStartBot.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0431\u043e\u0442\u0430", None))
        self.btnUpdateWidget.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.lblStatistics.setText("")
    # retranslateUi

