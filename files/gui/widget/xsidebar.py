from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QByteArray
from PyQt6.QtSvg import QSvgRenderer
import re
import files.app.config as config
import darkdetect

def get_theme_config(mode: str):
    style_config = config.STYLE_CONFIG_DARK if mode == "dark" else config.STYLE_CONFIG_LIGHT
    return {
        "bg_color": style_config["bg_color"],
        "text_color": style_config["text_color"],
        "button_bg": style_config["bg_color"],
        "button_hover": style_config["hover_bg"],
        "button_pressed": style_config["secondary_bg"],
        "font_family": style_config["font_family"],
        "font_size_medium": style_config["font_size_medium"],
        "separator_color": '#555555' if mode == "dark" else '#cccccc',
        "icon_color": '#f7f7f7' if mode == "dark" else '#1a1a1a'
    }

def change_svg_color(svg_data: str, new_color: str) -> str:
    return re.sub(r'fill=["\']#[0-9a-fA-F]{3,6}["\']', f'fill="{new_color}"', svg_data)

class SidebarButton(QPushButton):
    def __init__(self, icon_path=None, expanded_icon_path=None, full_text="", is_toggle=False, parent=None, theme=None):
        super().__init__(parent)
        self.icon_path = icon_path
        self.expanded_icon_path = expanded_icon_path or icon_path
        self.full_text = full_text
        self.is_toggle = is_toggle
        self.theme = theme or get_theme_config("dark")

        self.setIconSize(QSize(26, 26))
        self.setFixedHeight(50)
        self.set_expanded(False)
        self.apply_style(False)

    def apply_style(self, expanded: bool):
        alignment = "left" if expanded and not self.is_toggle else "center"
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.theme["button_bg"]};
                color: {self.theme["text_color"]};
                border: none;
                border-radius: 5px;
                padding: 5px;
                font: {self.theme["font_size_medium"]} "{self.theme["font_family"]}";
                margin: 2px;
                text-align: {alignment};
            }}
            QPushButton:hover {{
                background-color: {self.theme["button_hover"]};
            }}
            QPushButton:pressed {{
                background-color: {self.theme["button_pressed"]};
            }}
        """)
        self.update_icon(expanded)

    def update_icon(self, expanded: bool):
        path = self.expanded_icon_path if expanded and self.is_toggle else self.icon_path
        if path:
            with open(path, "r", encoding="utf-8") as f:
                svg_data = f.read()
            colored_svg = change_svg_color(svg_data, self.theme["icon_color"])
            renderer = QSvgRenderer(QByteArray(colored_svg.encode('utf-8')))
            pixmap = QPixmap(QSize(26, 26))
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            self.setIcon(QIcon(pixmap))

    def set_expanded(self, expanded: bool):
        if self.is_toggle:
            self.setText("")
        else:
            self.setIcon(QIcon())
            self.setText(self.full_text if expanded else "")
            self.setToolTip(self.full_text)
        self.update_icon(expanded)

class xSidebar(QFrame):
    def __init__(self, parent=None, theme_mode=None):
        super().__init__(parent)
        self.theme_mode = theme_mode or ("dark" if darkdetect.isDark() else "light")
        self.theme = get_theme_config(self.theme_mode)

        self.is_expanded = False
        self.min_width = 50
        self.max_width = 220

        self.setObjectName("xSidebar")
        self.setFixedWidth(self.min_width)
        self.setStyleSheet(f"""
            QFrame#xSidebar {{
                background-color: {self.theme["bg_color"]};
                border: none;
                border-radius: 7px;
            }}
        """)

        self._setup_ui()

    def _setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.toggle_btn = self._create_button("files/gui/icons/menu.svg", is_toggle=True)
        self.toggle_btn.clicked.connect(self.toggle_sidebar)
        self.layout.addWidget(self.toggle_btn)

        self.buttons = {
            "home": self._create_button("files/gui/icons/home.svg", full_text="Home"),
            "settings": self._create_button("files/gui/icons/settings.svg", full_text="Settings"),
        }

        self.layout.addWidget(self.buttons["home"])
        self.layout.addStretch()
        self.layout.addWidget(self.buttons["settings"])

    def _create_button(self, icon_path, full_text="", is_toggle=False):
        return SidebarButton(
            icon_path=icon_path,
            full_text=full_text,
            is_toggle=is_toggle,
            parent=self,
            theme=self.theme,
        )

    def toggle_sidebar(self):
        target_width = self.max_width if not self.is_expanded else self.min_width
        self._animate_sidebar(target_width)

        self.is_expanded = not self.is_expanded
        self._update_buttons()

    def _animate_sidebar(self, target_width):
        animation = QPropertyAnimation(self, b"minimumWidth")
        animation.setDuration(200)
        animation.setStartValue(self.width())
        animation.setEndValue(target_width)
        animation.start()
        self.animation = animation

    def _update_buttons(self):
        self.toggle_btn.set_expanded(self.is_expanded)
        self.toggle_btn.apply_style(self.is_expanded)
        for btn in self.buttons.values():
            btn.set_expanded(self.is_expanded)
            btn.apply_style(self.is_expanded)

    def set_theme(self, theme_mode):
        self.theme_mode = theme_mode
        self.theme = get_theme_config(theme_mode)

        self.setStyleSheet(f"""
            QFrame#xSidebar {{
                background-color: {self.theme["bg_color"]};
                border: none;
                border-radius: 7px;
            }}
        """)

        self.toggle_btn.theme = self.theme
        self.toggle_btn.apply_style(self.is_expanded)

        for btn in self.buttons.values():
            btn.theme = self.theme
            btn.apply_style(self.is_expanded)

# Note: Add your main block to run the app if needed, e.g.:
# if __name__ == "__main__":
#     from PyQt6.QtWidgets import QApplication
#     import sys
#     app = QApplication(sys.argv)
#     sidebar = xSidebar()
#     sidebar.show()
#     sys.exit(app.exec())