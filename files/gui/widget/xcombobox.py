# xcombobox.py
from PyQt6.QtWidgets import QComboBox

class xComboBox(QComboBox):
    def __init__(self, theme, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QComboBox {{
                background-color: {self.theme['secondary_bg']};
                border-radius: 6px;
                padding: 8px 12px;
                font: {self.theme['font_size_large']} "{self.theme['font_family']}";
                color: {self.theme['text_color']};
                min-height: 36px;
            }}
            QComboBox:hover {{
                background-color: {self.theme['hover_bg']};
            }}
            QComboBox:focus {{
                background-color: {self.theme['hover_bg']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 30px;
                background-color: transparent;
            }}
            QComboBox::down-arrow {{
                image: url(down_arrow.png);
                width: 16px;
                height: 16px;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {self.theme['secondary_bg']};
                border: 1px solid {self.theme['border_color']};
                border-radius: 6px;
                color: {self.theme['text_color']};
                padding: 4px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: 8px 12px;
                border-radius: 4px;
                background-color: {self.theme['secondary_bg']};
                color: {self.theme['text_color']};
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: {self.theme['accent_color']};
                color: {self.theme['selected_text_color']};
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {self.theme['selected_bg']};
                color: {self.theme['selected_text_color']};
                font-weight: bold;
            }}
        """)

    def update_theme(self, new_theme):
        """Update the theme and reapply the stylesheet."""
        self.theme = new_theme
        self.apply_theme()