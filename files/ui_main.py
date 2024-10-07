# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlmMxRv.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
import files.assest_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"    background-color: #1a2023;\n"
"    font: 600 20pt \"Segoe UI Variable Display Semib\";\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"\n"
"#leftMenu .QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:pressed {\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"#mainFrame {\n"
"    border: 2px solid #232a2f;	\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#mainFrame .QFrame {\n"
"\n"
"	background-color: #232a2f;\n"
"	\n"
"}\n"
"\n"
"#mainFrame .QLabel {\n"
"\n"
"	background-color: #232a2f;\n"
"	\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	\n"
"    padding: 7px;\n"
"    image-position: left center;\n"
"    font: 600 14pt \"Segoe UI Variable Display Semib\";\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#settings_btn {\n"
"    \n"
"	\n"
"	image: url(:/dark/assest/settings_48_regular.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"    \n"
"	image: url(:/icons/assest/home_48_regular.svg);"
                        "\n"
"}\n"
"\n"
"#theme_btn {\n"
"    image: url(:/leftMenu/Icons/light_theme_icon.svg);\n"
"}\n"
"\n"
"#menu_btn {\n"
"    image: url(:/leftMenu/Icons/menu_light.svg);\n"
"}\n"
"\n"
"#stg_lbl_main {\n"
"    padding-left: 4px;\n"
"    font: 700 24pt \"Segoe UI Variable Display\";\n"
"}\n"
"\n"
"#stack_stg .QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #4a4a4a; /* Updated for better contrast */\n"
"}\n"
"\n"
"#stg_home_app_bt_lbl {\n"
"    font: 600 13pt \"Segoe UI Variable Display Semib\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_app_img_lbl {\n"
"    \n"
"	image: url(:/leftMenu/Icons/light_theme_icon.svg);\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_app_hd_lbl {\n"
"    font: 900 16pt \"Segoe UI Black\";\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"#stg_home_app_img_btn {\n"
"    font: 600 14pt \"Segoe UI Variable Display Semib\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#stg_home_info_bt_lbl {\n"
"    font: 600 13pt \"Segoe UI Variable Display Semib\";\n"
"   "
                        " padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_info_img_lbl {\n"
"    image: url(:/leftMenu/Icons/light_info.svg);\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_info_hd_lbl {\n"
"    font: 900 16pt \"Segoe UI Black\";\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"#stg_home_info_img_btn {\n"
"    font: 600 14pt \"Segoe UI Variable Display Semib\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 7, 7, 7)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

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
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.verticalLayout_4 = QVBoxLayout(self.settings_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stg_lbl_v_frame_2 = QFrame(self.settings_page)
        self.stg_lbl_v_frame_2.setObjectName(u"stg_lbl_v_frame_2")
        self.stg_lbl_v_frame = QVBoxLayout(self.stg_lbl_v_frame_2)
        self.stg_lbl_v_frame.setSpacing(0)
        self.stg_lbl_v_frame.setObjectName(u"stg_lbl_v_frame")
        self.stg_lbl_v_frame.setContentsMargins(0, 0, 0, 0)
        self.stg_lbl_main = QLabel(self.stg_lbl_v_frame_2)
        self.stg_lbl_main.setObjectName(u"stg_lbl_main")
        self.stg_lbl_main.setMinimumSize(QSize(746, 43))
        self.stg_lbl_main.setMaximumSize(QSize(16777215, 43))

        self.stg_lbl_v_frame.addWidget(self.stg_lbl_main)

        self.stack_stg = QStackedWidget(self.stg_lbl_v_frame_2)
        self.stack_stg.setObjectName(u"stack_stg")
        self.stg_home_pg = QWidget()
        self.stg_home_pg.setObjectName(u"stg_home_pg")
        self.stack_stg.addWidget(self.stg_home_pg)
        self.stg_abt_pg = QWidget()
        self.stg_abt_pg.setObjectName(u"stg_abt_pg")
        self.verticalLayout_6 = QVBoxLayout(self.stg_abt_pg)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.stg_abt_pg)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.stg_home_app_hfrm = QFrame(self.verticalFrame)
        self.stg_home_app_hfrm.setObjectName(u"stg_home_app_hfrm")
        self.stg_home_app_hfrm.setMinimumSize(QSize(461, 69))
        self.stg_home_app_hfrm.setMaximumSize(QSize(16777215, 69))
        self.stg_home_app_hfrm.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border-radius: 7px;")
        self.horizontalLayout_2 = QHBoxLayout(self.stg_home_app_hfrm)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stg_home_app_img_lbl = QLabel(self.stg_home_app_hfrm)
        self.stg_home_app_img_lbl.setObjectName(u"stg_home_app_img_lbl")
        self.stg_home_app_img_lbl.setMinimumSize(QSize(69, 69))
        self.stg_home_app_img_lbl.setMaximumSize(QSize(69, 69))
        self.stg_home_app_img_lbl.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.stg_home_app_img_lbl)

        self.frame = QFrame(self.stg_home_app_hfrm)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stg_home_app_hd_lbl = QLabel(self.frame)
        self.stg_home_app_hd_lbl.setObjectName(u"stg_home_app_hd_lbl")
        self.stg_home_app_hd_lbl.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.stg_home_app_hd_lbl)

        self.stg_home_app_bt_lbl = QLabel(self.frame)
        self.stg_home_app_bt_lbl.setObjectName(u"stg_home_app_bt_lbl")
        self.stg_home_app_bt_lbl.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.stg_home_app_bt_lbl)


        self.horizontalLayout_2.addWidget(self.frame)

        self.stg_home_app_img_btn = QPushButton(self.stg_home_app_hfrm)
        self.stg_home_app_img_btn.setObjectName(u"stg_home_app_img_btn")
        self.stg_home_app_img_btn.setMinimumSize(QSize(69, 69))
        self.stg_home_app_img_btn.setMaximumSize(QSize(69, 69))
        self.stg_home_app_img_btn.setSizeIncrement(QSize(73, 0))
        self.stg_home_app_img_btn.setCheckable(False)
        self.stg_home_app_img_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.stg_home_app_img_btn)


        self.verticalLayout_5.addWidget(self.stg_home_app_hfrm)

        self.stg_home_info_hfrm = QFrame(self.verticalFrame)
        self.stg_home_info_hfrm.setObjectName(u"stg_home_info_hfrm")
        self.stg_home_info_hfrm.setMinimumSize(QSize(461, 69))
        self.stg_home_info_hfrm.setMaximumSize(QSize(16777215, 69))
        self.stg_home_info_hfrm.setStyleSheet(u"background-color: rgb(56, 56, 56);\n"
"border-radius: 7px;")
        self.horizontalLayout_3 = QHBoxLayout(self.stg_home_info_hfrm)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stg_home_info_img_lbl = QLabel(self.stg_home_info_hfrm)
        self.stg_home_info_img_lbl.setObjectName(u"stg_home_info_img_lbl")
        self.stg_home_info_img_lbl.setMinimumSize(QSize(69, 69))
        self.stg_home_info_img_lbl.setMaximumSize(QSize(69, 69))
        self.stg_home_info_img_lbl.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.stg_home_info_img_lbl)

        self.frame_2 = QFrame(self.stg_home_info_hfrm)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stg_home_info_hd_lbl = QLabel(self.frame_2)
        self.stg_home_info_hd_lbl.setObjectName(u"stg_home_info_hd_lbl")
        self.stg_home_info_hd_lbl.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.stg_home_info_hd_lbl)

        self.stg_home_info_bt_lbl = QLabel(self.frame_2)
        self.stg_home_info_bt_lbl.setObjectName(u"stg_home_info_bt_lbl")
        self.stg_home_info_bt_lbl.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.stg_home_info_bt_lbl)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.stg_home_info_img_btn = QPushButton(self.stg_home_info_hfrm)
        self.stg_home_info_img_btn.setObjectName(u"stg_home_info_img_btn")
        self.stg_home_info_img_btn.setMinimumSize(QSize(69, 69))
        self.stg_home_info_img_btn.setMaximumSize(QSize(69, 69))
        self.stg_home_info_img_btn.setSizeIncrement(QSize(73, 0))
        self.stg_home_info_img_btn.setCheckable(False)
        self.stg_home_info_img_btn.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.stg_home_info_img_btn)


        self.verticalLayout_5.addWidget(self.stg_home_info_hfrm)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.verticalFrame)

        self.stack_stg.addWidget(self.stg_abt_pg)
        self.stg_app_pg = QWidget()
        self.stg_app_pg.setObjectName(u"stg_app_pg")
        self.stack_stg.addWidget(self.stg_app_pg)

        self.stg_lbl_v_frame.addWidget(self.stack_stg)


        self.verticalLayout_4.addWidget(self.stg_lbl_v_frame_2)

        self.switchPage.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_3 = QVBoxLayout(self.info_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.switchPage.addWidget(self.info_page)

        self.verticalLayout_2.addWidget(self.switchPage)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.switchPage.setCurrentIndex(1)
        self.stack_stg.setCurrentIndex(1)


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
        self.theme_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Theme", None))
#endif // QT_CONFIG(tooltip)
        self.theme_btn.setText("")
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText("")
        self.stg_lbl_main.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.stg_home_app_img_lbl.setText("")
        self.stg_home_app_hd_lbl.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.stg_home_app_bt_lbl.setText(QCoreApplication.translate("MainWindow", u"app version, developer", None))
        self.stg_home_app_img_btn.setText("")
        self.stg_home_info_img_lbl.setText("")
        self.stg_home_info_hd_lbl.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.stg_home_info_bt_lbl.setText(QCoreApplication.translate("MainWindow", u"More details", None))
        self.stg_home_info_img_btn.setText("")
    # retranslateUi

