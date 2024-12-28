# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindYBSxp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
import assest_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Light Theme */\n"
"\n"
"\n"
"* {\n"
"	/*background-color : #f3f3f3;*/\n"
"	font: 600 20pt \"Consolas\";\n"
"	color : #202325;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	background-color: transparent;\n"
"	border-radius : 7px;\n"
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
"	border : 2px solid #e5e5e5;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#mainFrame .QFrame {\n"
"\n"
"	background-color: #f6f8fa;\n"
"	\n"
"}\n"
"\n"
"#mainFrame .QLabel {\n"
"\n"
"	background-color: #f6f8fa;\n"
"	\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	padding : 7px;\n"
"	image-position: left center;\n"
"	font:  13pt \"Consolas\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#settings_btn {\n"
"    \n"
"	image: url(:/light/light/settings_48_regular.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"    \n"
"	\n"
"	image: url(:/light/light/home_48_regular.svg);\n"
"}\n"
"\n"
"#theme_btn {\n"
"    \n"
"	image"
                        ": url(:/light/light/weather_sunny_48_regular.svg);\n"
"}\n"
"\n"
"#menu_btn {\n"
"    \n"
"	image: url(:/light/light/panel_left_text_48_regular.svg);\n"
"}\n"
"\n"
"#home_page {\n"
"	background-color: #f6f8fa;\n"
"}\n"
"#setting_page {\n"
"	background-color: #f6f8fa;\n"
"}\n"
"#info_page {\n"
"	background-color: #f6f8fa;\n"
"}\n"
"\n"
"#stg_lbl_main {\n"
"    padding-left: 4px;\n"
"    font: 700 24pt \"Consolas\";\n"
"}\n"
"\n"
"#stg_home_app_bt_lbl {\n"
"    font: 600 13pt \"Consolas\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_app_hd_lbl {\n"
"    font: 900 16pt \"Consolas\";\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"#stg_home_app_img_lbl {\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_abt_pg{\n"
"	background-color: #f6f8fa;\n"
"}\n"
"\n"
"#stg_home_pg{\n"
"	background-color: #f6f8fa;\n"
"}\n"
"\n"
"#stg_app_pg{\n"
"	background-color: #f6f8fa;\n"
"}\n"
"\n"
"#stack_stg .QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #e5e5e5;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 7, 7, 7)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(50, 0))
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
        self.mainFrame.setStyleSheet(u"border-radius: 7px;")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.switchPage = QStackedWidget(self.mainFrame)
        self.switchPage.setObjectName(u"switchPage")
        self.switchPage.setStyleSheet(u"")
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

        self.setting_stackfrm = QStackedWidget(self.stg_lbl_v_frame_2)
        self.setting_stackfrm.setObjectName(u"setting_stackfrm")
        self.setting_stackfrm.setStyleSheet(u"")
        self.stg_home_pg = QWidget()
        self.stg_home_pg.setObjectName(u"stg_home_pg")
        self.setting_stackfrm.addWidget(self.stg_home_pg)
        self.stg_abt_pg = QWidget()
        self.stg_abt_pg.setObjectName(u"stg_abt_pg")
        self.verticalLayout_6 = QVBoxLayout(self.stg_abt_pg)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.setting_stackfrm.addWidget(self.stg_abt_pg)
        self.stg_app_pg = QWidget()
        self.stg_app_pg.setObjectName(u"stg_app_pg")
        self.setting_stackfrm.addWidget(self.stg_app_pg)

        self.stg_lbl_v_frame.addWidget(self.setting_stackfrm)


        self.verticalLayout_4.addWidget(self.stg_lbl_v_frame_2)

        self.switchPage.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.switchPage.addWidget(self.info_page)

        self.verticalLayout_2.addWidget(self.switchPage)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.switchPage.setCurrentIndex(1)
        self.setting_stackfrm.setCurrentIndex(1)


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
    # retranslateUi

