# main.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget, QGraphicsOpacityEffect
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from files.gui.modules import *
from files.app.app_functions import *
import files.app.config as config
from files.gui.ui_components import *
from files.gui.pages.home import HomePage
from files.gui.pages.settings import SettingsPage
from PyQt6.QtGui import QIcon, QAction
import os
import shutil
import uuid
import hashlib
import base64
import darkdetect
from PyQt6.QtWidgets import QVBoxLayout

theme_dark = config.STYLE_CONFIG_DARK
theme_light = config.STYLE_CONFIG_LIGHT
config_theme = config.SETTINGS["theme"]
is_menubar = config.SETTINGS["menu_bar_enabled"]
is_mica = config.SETTINGS["is_mica"]
passMinSize = 4

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(config.SETTINGS["app"]["name"])
        # self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 700, 500)

        
        if config_theme == "default":
            self.current_theme = theme_dark if darkdetect.isDark() else theme_light
        
            # print(config_theme)
        elif config_theme == "dark":
            self.current_theme = theme_dark
            try:
                if is_mica:
                    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                    ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)
            except Exception as e:
                print(f"Failed to apply Mica effect: {e}")
                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)

        else:
            self.current_theme = theme_light
            try:
                if is_mica:
                    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                    ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)
            except Exception as e:
                print(f"Failed to apply Mica effect: {e}")
                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
            
        self.setup_ui()

        if os.name == "nt":
            try:
                if is_mica:
                    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                    ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)
            except Exception as e:
                print(f"Failed to apply Mica effect: {e}")
                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)

    def setup_ui(self):
        if is_menubar:
            self.menu_bar = xMenuBar(self.current_theme, self)
            self.setMenuBar(self.menu_bar)

        container = QWidget()
        main_layout = QHBoxLayout(container)
        main_layout.setSpacing(10)

        self.sidebar = xSidebar(self, theme_mode="dark" if self.current_theme == theme_dark else "light")
        self.sidebar.setFixedWidth(50)
        main_layout.addWidget(self.sidebar)

        self.stack_widget = QStackedWidget()

        self.home_page = HomePage(self, self.current_theme)
        self.settings_page = SettingsPage(self, self.current_theme)
        self.stack_widget.addWidget(self.home_page)
        self.stack_widget.addWidget(self.settings_page)
        self.stack_widget.setCurrentWidget(self.settings_page)
        self.sidebar.set_active_button("settings")

        self.sidebar.buttons["home"].clicked.connect(self.show_home_page)
        self.sidebar.buttons["settings"].clicked.connect(self.show_settings_page)
        self.sidebar.buttons["theme"].clicked.connect(self.toggle_theme)

        main_layout.addWidget(self.stack_widget)
        self.setCentralWidget(container)
        self.apply_theme()

    def show_home_page(self):
        self.stack_widget.setCurrentWidget(self.home_page)
        self.sidebar.set_active_button("home")  # or "settings", etc.
        print("Home page displayed")

    def show_settings_page(self):
        self.stack_widget.setCurrentWidget(self.settings_page)
        self.sidebar.set_active_button("settings")  # or "home", etc.
        print("Settings page displayed")

    def apply_theme(self):
        self.home_page.apply_theme(self.current_theme)
        self.settings_page.apply_theme(self.current_theme)
        self.stack_widget.setStyleSheet(
    f"background-color: {self.current_theme['secondary_bg']}; "
    "border-radius: 5px;"
)
        self.setStyleSheet(f"background-color: {self.current_theme['bg_color']};")
        if is_menubar:
            self.menu_bar.update_theme(self.current_theme)
        self.sidebar.set_theme("light" if self.current_theme == theme_light else "dark")

    def toggle_theme(self):
        self.current_theme = theme_light if self.current_theme == theme_dark else theme_dark
        self.home_page.theme_toggle.setText("Dark" if self.current_theme == theme_light else "Light")

        self.sidebar.set_theme("light" if self.current_theme == theme_light else "dark")
        self.sidebar.buttons["theme"].icon_path = f"files/gui/icons/{'sun_half' if self.current_theme == theme_light else 'moon_half'}.svg"
        self.sidebar.buttons["theme"].update_icon(self.sidebar.is_expanded)
        self.apply_theme()
        self.home_page.apply_theme(self.current_theme)
        self.settings_page.apply_theme(self.current_theme)
        if hasattr(self.sidebar, 'refresh_theme'):
            self.sidebar.refresh_theme(self.current_theme)
        if os.name == "nt":
            try:
                ApplyMica(
                    int(self.winId()),
                    Theme=MicaTheme.LIGHT if self.current_theme == theme_light else MicaTheme.DARK,
                    Style=MicaStyle.DEFAULT
                )
            except Exception as e:
                print(f"Failed to update Mica theme: {e}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Auto-collapse sidebar if width is small, expand if large
        threshold = 600
        if self.width() < threshold:
            self.sidebar.set_expanded_state(False)
        else:
            self.sidebar.set_expanded_state(True)

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())