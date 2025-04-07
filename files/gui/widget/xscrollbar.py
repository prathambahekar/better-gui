# custom_scrollbar.py
from PyQt6.QtWidgets import QScrollBar
from PyQt6.QtCore import Qt

class xScrollBar(QScrollBar):
    def __init__(self, theme, parent=None):
        super().__init__(Qt.Orientation.Vertical, parent)
        self.current_theme = theme
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QScrollBar:vertical {{
                border: none;
                background: transparent;
                width: 8px;  /* Slim, like Windows 11 */
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: rgba(150, 150, 150, 100);  /* Semi-transparent gray */
                min-height: 20px;
                border-radius: 4px;  /* Rounded edges */
            }}
            QScrollBar::handle:vertical:hover {{
                background: rgba(180, 180, 180, 150);  /* Lighter on hover */
            }}
            QScrollBar::handle:vertical:pressed {{
                background: rgba(200, 200, 200, 180);  /* Even lighter when pressed */
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;  /* Hide arrows */
                background: none;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;  /* No track background */
            }}
        """)

    def update_theme(self, new_theme):
        self.current_theme = new_theme
        self.apply_theme()