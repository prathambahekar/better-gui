# xbutton.py
from PyQt6.QtWidgets import QPushButton
import files.app.config as config
import darkdetect




class xButton(QPushButton):
    def __init__(self, text, theme, parent=None):
        super().__init__(text, parent)
        self.theme = theme
        self.theme['accent_color'] = config.STYLE_CONFIG_DARK["accent_color"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["accent_color"]

        self.theme['selected_text_color'] = config.STYLE_CONFIG_DARK["selected_text_color"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["selected_text_color"]

        self.theme['accent_hover'] = config.STYLE_CONFIG_DARK["accent_hover"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["accent_hover"]

        self.theme['font_family'] = config.STYLE_CONFIG_DARK["font_family"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["font_family"]

        self.theme['font_size_medium'] = config.STYLE_CONFIG_DARK["font_size_medium"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["font_size_medium"]

        self.theme['accent_pressed'] = config.STYLE_CONFIG_DARK["accent_pressed"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["accent_pressed"]

        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.theme['accent_color']};
                color: {self.theme['selected_text_color']};
                padding: 10px 20px;
                font: {self.theme['font_size_medium']} "{self.theme['font_family']}";
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: {self.theme['accent_hover']};
            }}
            QPushButton:pressed {{
                background-color: {self.theme['accent_pressed']};
            }}
        """)

    def update_theme(self, new_theme):
        """Update the theme and reapply the stylesheet."""
        self.theme = new_theme
        self.apply_theme()