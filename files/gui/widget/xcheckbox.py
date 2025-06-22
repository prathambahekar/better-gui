from PyQt6.QtWidgets import QCheckBox

class xCheckBox(QCheckBox):
    def __init__(self, text, theme, parent=None):
        super().__init__(text, parent)
        self.theme = theme
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f'''
            QCheckBox {{
                font: {self.theme['font_size_title']} "{self.theme['font_family']}";
                color: {self.theme['text_color']};
                padding-left: 6px;
            }}
            QCheckBox::indicator {{
                width: 38px;
                height: 20px;
            }}
            QCheckBox::indicator:unchecked {{
                border-radius: 10px;
                background: #c6c6c6;
                border: 1px solid #b0b0b0;
            }}
            QCheckBox::indicator:checked {{
                border-radius: 10px;
                background: {self.theme['accent_color']};
                border: 1px solid {self.theme['accent_color']};
            }}
            QCheckBox::indicator:unchecked:pressed,
            QCheckBox::indicator:checked:pressed {{
                background: #a0a0a0;
            }}
        ''')

    def update_theme(self, new_theme):
        self.theme = new_theme
        self.apply_theme() 