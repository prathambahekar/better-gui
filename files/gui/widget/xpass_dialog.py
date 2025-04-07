from files.gui.modules import *
import files.app.config as config


theme_dark = config.STYLE_CONFIG_DARK
theme_light = config.STYLE_CONFIG_LIGHT


class PasswordDialog(QDialog):
    def __init__(self, title, prompt, parent=None, theme=theme_dark):
        super().__init__(parent)
        self.setWindowTitle(title)
        layout = QVBoxLayout(self)
        label = QLabel(prompt)
        layout.addWidget(label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumWidth(300)
        layout.addWidget(self.password_input)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.apply_theme(theme)

    def apply_theme(self, theme):
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {theme['bg_color']};
                color: {theme['text_color']};
            }}
            QLineEdit {{
                background-color: {theme['secondary_bg']};
                color: {theme['text_color']};
                padding: 10px;
                border: 1px solid {theme['border_color']};
                border-radius: 5px;
            }}
            QLabel {{
                color: {theme['text_color']};
                font: {theme['font_size_medium']} "{theme['font_family']}";
            }}
            QPushButton {{
                background-color: {theme['accent_color']};
                color: {theme['selected_text_color']};
                padding: 10px;
                font: {theme['font_size_medium']} "{theme['font_family']}";
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: {theme['accent_hover']};
            }}
        """)