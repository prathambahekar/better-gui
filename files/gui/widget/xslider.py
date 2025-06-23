from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt

class xSlider(QSlider):
    def __init__(self, theme, parent=None):
        super().__init__(Qt.Orientation.Horizontal, parent)
        self.theme = theme
        self.setMinimumHeight(28)
        self.setMaximumHeight(36)
        self.update_theme(theme)

    def update_theme(self, theme):
        self.theme = theme
        accent = self.theme.get('accent_color', '#2563eb')
        groove_bg = self.theme.get('slider_groove_bg', '#e5e5e5')
        groove_fill = accent
        handle_bg = '#fff'
        handle_border = accent
        groove_height = 6
        handle_radius = 12
        handle_size = 24
        self.setStyleSheet(f"""
            QSlider {{
                background: transparent;
            }}
            QSlider::groove:horizontal {{
                border: none;
                height: {groove_height}px;
                background: {groove_bg};
                border-radius: {groove_height//2}px;
            }}
            QSlider::sub-page:horizontal {{
                background: {groove_fill};
                border-radius: {groove_height//2}px;
            }}
            QSlider::add-page:horizontal {{
                background: {groove_bg};
                border-radius: {groove_height//2}px;
            }}
            QSlider::handle:horizontal {{
                background: {handle_bg};
                border: 2px solid {handle_border};
                width: {handle_size}px;
                height: {handle_size}px;
                margin: -{handle_size//2 - groove_height//2}px 0;
                border-radius: {handle_radius}px;
                /* box-shadow: 0 2px 8px rgba(0,0,0,0.10); */
                transition: border 0.2s, background 0.2s;
            }}
            QSlider::handle:horizontal:hover {{
                background: {accent};
                border: 2px solid {accent};
            }}
        """) 