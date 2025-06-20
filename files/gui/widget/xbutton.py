# xbutton.py
from PyQt6.QtWidgets import QPushButton
import files.app.config as config
import darkdetect
from files.gui.theme import PRIMARY_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, PADDING, BORDER_RADIUS




class xButton(QPushButton):
    """
    A consistent, theme-aware button for the application.
    Usage: Simply instantiate xButton(text, parent) and it will use the app's theme.
    """
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {PRIMARY_COLOR};
                color: {TEXT_COLOR};
                padding: {PADDING}px {PADDING*2}px;
                font: {FONT_SIZE}px \"{FONT_FAMILY}\";
                border-radius: {BORDER_RADIUS}px;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
            QPushButton:pressed {{
                background-color: #2471a3;
            }}
        """)

    def update_theme(self):
        """Reapply the stylesheet (for dynamic theme changes)."""
        self.apply_theme()