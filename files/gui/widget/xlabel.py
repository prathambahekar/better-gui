# xlabel.py
from PyQt6.QtWidgets import QLabel

class xLabel(QLabel):
    def __init__(self, text, theme, parent=None):
        super().__init__(text, parent)
        self.theme = theme
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel {{
                background : transparent;
                font: bold {self.theme['font_size_title']} "{self.theme['font_family']}";
                color: {self.theme['text_color']};
                padding: 10px;
            }}
        """)

    def update_theme(self, new_theme):
        """Update the theme and reapply the stylesheet."""
        self.theme = new_theme
        self.apply_theme()