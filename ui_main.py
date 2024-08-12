# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHVbwWV.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	background-color : #f9f9f9;\n"
"	font: 600 20pt \"Segoe UI Variable Display Semib\";\n"
"}\n"
"\n"
"#leftMenu {\n"
"	background : #f3f3f3;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	border-radius : 7px;\n"
"\n"
"}\n"
"\n"
"#leftMenu .QPushButton:hover {\n"
"	background-color: #ededed;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:pressed {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#mainFrame {\n"
"	border-left : 2px solid #e5e5e5;\n"
"	border-top : 2px solid #e5e5e5;\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom : transparent;\n"
"	border-right : transparent;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"		padding : 7px;\n"
"}\n"
"\n"
"#settings_btn {\n"
"	image: url(:/leftMenu/Icons/regular_settings_dark.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"	image: url(:/leftMenu/Icons/regular_home_dark.svg);\n"
"}\n"
"\n"
"#theme_btn {\n"
"	\n"
"	image: url(:/leftMenu/Icons/dark_theme_icon.svg);\n"
"}\n"
"\n"
"#menu_btn {\n"
"	image: url(:/leftMenu/Icons/menu_dark.sv"
                        "g);\n"
"}\n"
"\n"
"#info_btn {\n"
"	image: url(:/leftMenu/Icons/dark_info.svg);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(50, 16777215))
        self.leftMenu.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.menu_btn = QPushButton(self.leftMenu)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMaximumSize(QSize(16777215, 40))
        self.menu_btn.setStyleSheet(u"image-position : center")

        self.verticalLayout.addWidget(self.menu_btn)

        self.home_btn = QPushButton(self.leftMenu)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy)
        self.home_btn.setMaximumSize(QSize(16777215, 40))
        self.home_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.home_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.info_btn = QPushButton(self.leftMenu)
        self.info_btn.setObjectName(u"info_btn")
        sizePolicy.setHeightForWidth(self.info_btn.sizePolicy().hasHeightForWidth())
        self.info_btn.setSizePolicy(sizePolicy)
        self.info_btn.setMaximumSize(QSize(16777215, 40))
        self.info_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.info_btn)

        self.theme_btn = QPushButton(self.leftMenu)
        self.theme_btn.setObjectName(u"theme_btn")
        sizePolicy.setHeightForWidth(self.theme_btn.sizePolicy().hasHeightForWidth())
        self.theme_btn.setSizePolicy(sizePolicy)
        self.theme_btn.setMaximumSize(QSize(16777215, 40))
        self.theme_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.theme_btn)

        self.settings_btn = QPushButton(self.leftMenu)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMaximumSize(QSize(16777215, 40))
        self.settings_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.settings_btn)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.switchPage = QStackedWidget(self.mainFrame)
        self.switchPage.setObjectName(u"switchPage")
        self.switchPage.setStyleSheet(u"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.switchPage.addWidget(self.home_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.switchPage.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_3 = QVBoxLayout(self.info_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.about_lbl = QLabel(self.info_page)
        self.about_lbl.setObjectName(u"about_lbl")
        self.about_lbl.setMinimumSize(QSize(0, 61))
        self.about_lbl.setMaximumSize(QSize(16777215, 80))
        self.about_lbl.setStyleSheet(u"font: 600 25pt \"Segoe UI Variable Display Semib\";")
        self.about_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.about_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.version_lbl = QLabel(self.info_page)
        self.version_lbl.setObjectName(u"version_lbl")
        self.version_lbl.setMinimumSize(QSize(0, 100))
        self.version_lbl.setMaximumSize(QSize(16777215, 100))
        self.version_lbl.setStyleSheet(u"")
        self.version_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.version_lbl)

        self.build_lbl = QLabel(self.info_page)
        self.build_lbl.setObjectName(u"build_lbl")
        self.build_lbl.setMinimumSize(QSize(0, 100))
        self.build_lbl.setMaximumSize(QSize(16777215, 100))
        self.build_lbl.setStyleSheet(u"")
        self.build_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.build_lbl)

        self.creator_lbl = QLabel(self.info_page)
        self.creator_lbl.setObjectName(u"creator_lbl")
        self.creator_lbl.setMinimumSize(QSize(0, 100))
        self.creator_lbl.setMaximumSize(QSize(16777215, 100))
        self.creator_lbl.setStyleSheet(u"")
        self.creator_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.creator_lbl)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.switchPage.addWidget(self.info_page)

        self.verticalLayout_2.addWidget(self.switchPage)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.switchPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText("")
#if QT_CONFIG(tooltip)
        self.info_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Theme", None))
#endif // QT_CONFIG(tooltip)
        self.info_btn.setText("")
#if QT_CONFIG(tooltip)
        self.theme_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Theme", None))
#endif // QT_CONFIG(tooltip)
        self.theme_btn.setText("")
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText("")
        self.about_lbl.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.version_lbl.setText(QCoreApplication.translate("MainWindow", u"Version - 1.0.0", None))
        self.build_lbl.setText(QCoreApplication.translate("MainWindow", u"Build - Stable", None))
        self.creator_lbl.setText(QCoreApplication.translate("MainWindow", u"Developer - Pratham Bahekar", None))
    # retranslateUi

