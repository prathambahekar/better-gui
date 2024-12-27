# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainvQwtGv.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import assest_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Dark Theme */\n"
"\n"
"* {\n"
"    /*background-color: #1b1b1b;*/\n"
"    font: 600 20pt \"Consolas\";\n"
"    color: #e0e0e0;\n"
"}\n"
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
"    border: 2px solid #202326;	\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#mainFrame .QFrame {\n"
"\n"
"	background-color: #1e1e1e;\n"
"	\n"
"}\n"
"\n"
"#mainFrame .QLabel {\n"
"\n"
"	background-color: #1e1e1e;\n"
"	\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	\n"
"    padding: 7px;\n"
"    image-position: left center;\n"
"    font:  13pt \"Consolas\";\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#settings_btn {\n"
"    \n"
"	image: url(:/dark/dark/settings_48_regular.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"    \n"
"	\n"
"	image: url(:/dark/dark/home_48_regular.svg);\n"
"}\n"
"\n"
"#theme_btn {\n"
""
                        "    \n"
"	image: url(:/dark/dark/weather_sunny_48_regular.svg);\n"
"}\n"
"\n"
"#menu_btn {\n"
"    \n"
"	image: url(:/dark/dark/panel_left_text_48_regular.svg);\n"
"}\n"
"\n"
"#stg_lbl_main {\n"
"    padding-left: 4px;\n"
"    font: 700 24pt \"Consolas\";\n"
"}\n"
"\n"
"#stack_stg .QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #4a4a4a;\n"
"}\n"
"\n"
"#stg_home_app_bt_lbl {\n"
"    font: 600 13pt \"Consolas Semib\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_app_img_lbl {\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_app_hd_lbl {\n"
"    font: 900 16pt \"Consolas\";\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"#stg_home_app_img_btn {\n"
"    font: 600 14pt \"Consolas\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#stg_home_info_bt_lbl {\n"
"    font: 600 13pt \"Consolas\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_info_img_lbl {\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_info_hd_lbl {\n"
"    font: 900 16pt \"Consolas\";\n"
"    padding-left: 2px;\n"
"}"
                        "\n"
"\n"
"#stg_home_info_img_btn {\n"
"    font: 600 14pt \"Consolas\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#home_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"#setting_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"#info_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_abt_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_home_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_app_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
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
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.home_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_2 = QScrollArea(self.home_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 721, 564))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.comboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_5.addWidget(self.comboBox)

        self.radioButton_2 = QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_5.addWidget(self.radioButton_2)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_5.addWidget(self.checkBox_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

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
        self.scrollArea = QScrollArea(self.info_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(420, 130, 261, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 261, 321))
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 201, 51))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget = QTabWidget(self.info_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 30, 351, 451))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(60, 120, 241, 71))
        self.radioButton = QRadioButton(self.tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(80, 240, 151, 61))
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 50, 171, 61))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.switchPage.addWidget(self.info_page)

        self.verticalLayout_2.addWidget(self.switchPage)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.switchPage.setCurrentIndex(0)
        self.setting_stackfrm.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


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
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.stg_lbl_main.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lineEdit.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

