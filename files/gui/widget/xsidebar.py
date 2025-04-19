from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QIcon, QPixmap
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QByteArray, QEasingCurve, QRect
from PyQt6.QtSvg import QSvgRenderer
import re
import files.app.config as config
import darkdetect

# Constants
BUTTON_ICON_SIZE = QSize(25, 25)
BUTTON_HEIGHT = 45
SIDEBAR_MIN_WIDTH = 50
SIDEBAR_MAX_WIDTH = 220


def get_theme_config(mode: str):
    style_config = config.STYLE_CONFIG_DARK if mode == "dark" else config.STYLE_CONFIG_LIGHT
    return {
        "bg_color": style_config["bg_color"],
        "text_color": style_config["text_color"],
        "button_bg": style_config["bg_color"],
        "button_hover": style_config["hover_bg"],
        "button_pressed": style_config["secondary_bg"],
        "button_active_bg": "#252525" if mode == "dark" else "#e0e0e0",
        "font_family": style_config["font_family"],
        "font_size_medium": style_config["font_size_medium"],
        "separator_color": '#555555' if mode == "dark" else '#cccccc',
        "icon_color": '#f7f7f7' if mode == "dark" else '#1a1a1a',
        "accent_color": style_config["accent_color"]
    }


def change_svg_color(svg_data: str, new_color: str) -> str:
    svg_data = re.sub(r'fill=["\']#[0-9a-fA-F]{3,6}["\']', f'fill="{new_color}"', svg_data)
    svg_data = re.sub(r'style="[^"]*fill:[^;\"]+;?', f'style="fill:{new_color};', svg_data)
    return svg_data


def apply_sidebar_style(widget, theme):
    widget.setStyleSheet(f"""
        background-color: {theme["bg_color"]};
        border: none;
        border-radius: 7px;
    """)


class SidebarButton(QPushButton):
    def __init__(self, icon_path=None, expanded_icon_path=None, full_text="", is_toggle=False, parent=None, theme=None):
        super().__init__(parent)
        self.icon_path = icon_path
        self.expanded_icon_path = expanded_icon_path or icon_path
        self.full_text = full_text
        self.is_toggle = is_toggle
        self.theme = theme or {}
        self.active = False

        self.setIconSize(BUTTON_ICON_SIZE)
        self.setFixedHeight(BUTTON_HEIGHT)

        self.accent_bar = QWidget(self)
        self.accent_bar.setFixedWidth(3)
        self.accent_bar.setStyleSheet(f"""background: {self.theme["accent_color"]}; border-radius: 1px;""")
        self.accent_bar.hide()

        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(0)
        glow.setOffset(0)
        glow.setColor(Qt.GlobalColor.magenta)
        self.accent_bar.setGraphicsEffect(glow)

        self.set_expanded(False)
        self.apply_style(False)
        self.clicked.connect(self.animate_click)

    def set_active(self, is_active: bool):
        self.active = is_active
        if is_active:
            self.accent_bar.show()
            self.animate_accent()
        else:
            self.accent_bar.hide()
        self.apply_style(expanded=self.text() != "")

    def apply_style(self, expanded: bool):
        alignment = "left" if expanded and not self.is_toggle else "center"
        base_bg = self.theme.get("button_bg", "#222")
        active_bg = self.theme.get("button_active_bg", "#333")
        current_bg = active_bg if self.active else base_bg

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {current_bg};
                color: {self.theme.get("text_color", "#fff")};
                border: none;
                border-radius: 7px;
                padding: 5px;
                font: {self.theme.get("font_size_medium", "13px")} "{self.theme.get("font_family", "Segoe UI")}";
                margin: 2px;
                text-align: {alignment};
            }}
            QPushButton:hover {{
                background-color: {self.theme.get("button_hover", "#444")};
            }}
            QPushButton:pressed {{
                background-color: {self.theme.get("button_pressed", "#555")};
            }}
        """)
        self.update_icon(expanded)

    def refresh_theme(self, new_theme):
        self.theme = new_theme
        self.apply_style(self.text() != "")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.position_accent_bar()

    def position_accent_bar(self):
        if not self.accent_bar.isVisible():
            return
        bar_height = self.height() // 3
        self.accent_bar.setFixedHeight(bar_height)
        self.accent_bar.move(0, (self.height() - bar_height) // 2)

    def animate_accent(self):
        self.position_accent_bar()
        self.anim = QPropertyAnimation(self.accent_bar, b"geometry")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        start_rect = QRect(0, self.height() // 2, 5, 0)
        end_rect = QRect(0, (self.height() - self.accent_bar.height()) // 2, 5, self.accent_bar.height())
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.start()

    def update_icon(self, expanded: bool):
        path = self.expanded_icon_path if expanded and self.is_toggle else self.icon_path
        if path:
            with open(path, "r", encoding="utf-8") as f:
                svg_data = f.read()
            colored_svg = change_svg_color(svg_data, self.theme.get("icon_color", "#fff"))
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

    def animate_click(self):
        self.click_anim = QPropertyAnimation(self, b"size")
        self.click_anim.setDuration(150)
        self.click_anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        original_size = self.size()
        shrunk_size = original_size - QSize(7, 7)
        self.click_anim.setStartValue(original_size)
        self.click_anim.setEndValue(original_size)
        self.click_anim.setKeyValueAt(0.5, shrunk_size)
        self.click_anim.start()


class xSidebar(QFrame):
    def __init__(self, parent=None, theme_mode=None):
        super().__init__(parent)
        self.theme_mode = theme_mode or ("dark" if darkdetect.isDark() else "light")
        self.theme = get_theme_config(self.theme_mode)

        self.is_expanded = False
        self.active_button_key = None

        self.setObjectName("xSidebar")
        self.setMinimumWidth(SIDEBAR_MIN_WIDTH)
        apply_sidebar_style(self, self.theme)

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
            "theme": self._create_button("files/gui/icons/sun_half.svg", full_text="Theme"),
        }

        self.layout.addWidget(self.buttons["home"])
        self.layout.addStretch()
        self.layout.addWidget(self.buttons["theme"])
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
        target_width = SIDEBAR_MAX_WIDTH if not self.is_expanded else SIDEBAR_MIN_WIDTH
        self._animate_sidebar(target_width)
        self.is_expanded = not self.is_expanded
        self._update_buttons()

    def _animate_sidebar(self, target_width):
        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(target_width)
        self.animation.start()

    def _update_buttons(self):
        self.toggle_btn.set_expanded(self.is_expanded)
        self.toggle_btn.apply_style(self.is_expanded)
        for btn in self.buttons.values():
            btn.set_expanded(self.is_expanded)
            btn.apply_style(self.is_expanded)

    def set_theme(self, theme_mode):
        self.theme_mode = theme_mode
        self.theme = get_theme_config(theme_mode)
        apply_sidebar_style(self, self.theme)

        self.toggle_btn.refresh_theme(self.theme)
        for btn in self.buttons.values():
            btn.refresh_theme(self.theme)

    def toggle_theme(self):
        new_theme = "light" if self.theme_mode == "dark" else "dark"
        self.set_theme(new_theme)
        self.buttons["theme"].icon_path = f"files/gui/icons/{'moon_half' if new_theme == 'dark' else 'sun_half'}.svg"
        self.buttons["theme"].update_icon(self.is_expanded)

    def set_active_button(self, key):
        for name, btn in self.buttons.items():
            btn.set_active(name == key)
        self.active_button_key = key
