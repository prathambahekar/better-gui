# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainhNYGtw.ui'
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
import files.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"    background-color: #2b2b2b;\n"
"    font: 600 20pt \"Segoe UI Variable Display Semib\";\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"#leftMenu {\n"
"    background: #1e1e1e;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:pressed {\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"#mainFrame {\n"
"    border-left: 2px solid #1b1b1b;\n"
"    border-top: 2px solid #1b1b1b;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom: transparent;\n"
"    border-right: transparent;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"    padding: 7px;\n"
"    image-position: left center;\n"
"    font: 600 14pt \"Segoe UI Variable Display Semib\";\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#settings_btn {\n"
"    image: url(:/leftMenu/Icons/regular_settings_light.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"    image: url(:/leftMenu/Icons/regular_home_light"
                        ".svg);\n"
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
"#info_btn {\n"
"    image: url(:/leftMenu/Icons/light_info.svg);\n"
"}\n"
"\n"
"#stg_lbl_main {\n"
"	padding-left: 4px;\n"
"	font: 700 24pt \"Segoe UI Variable Display\";\n"
"}\n"
"\n"
"#stack_stg .QWidget{\n"
"	\n"
"border-radius: 8px;\n"
"background-color: #383838;	\n"
"\n"
"\n"
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
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.horizontalFrame = QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(461, 69))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 69))
        self.horizontalFrame.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #383838;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(69, 69))
        self.label.setMaximumSize(QSize(69, 69))
        self.label.setStyleSheet(u"image: url(:/leftMenu/Icons/light_info.svg);\n"
"padding: 10px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 900 16pt \"Segoe UI Black\";\n"
"padding-left: 2px;")

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 600 13pt \"Segoe UI Variable Display Semib\";\n"
"padding-left: 16px;")

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.pushButton = QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(69, 69))
        self.pushButton.setMaximumSize(QSize(69, 69))
        self.pushButton.setSizeIncrement(QSize(73, 0))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.horizontalFrame)

        self.horizontalFrame_2 = QFrame(self.verticalFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(461, 69))
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 69))
        self.horizontalFrame_2.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #383838;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_5.addWidget(self.horizontalFrame_2)

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
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"app version, developer", None))
        self.pushButton.setText("")
    # retranslateUi

