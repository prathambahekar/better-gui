import os
import json
import base64
import hashlib
import uuid
import shutil
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox
import files.app.config as config

# Access the variables using dot notation
theme_dark = config.STYLE_CONFIG_DARK
theme_light = config.STYLE_CONFIG_LIGHT

class AppFunctions:
    @staticmethod
    def show_message(parent, message, title, theme=theme_dark):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        stylesheet = f"""
            QMessageBox {{
                background-color: {theme['bg_color']};
                color: {theme['text_color']};
                font: {theme['font_size_large']} "{theme['font_family']}";
                border-radius: 10px;
                padding: 20px;
            }}
            QMessageBox QPushButton {{
                background-color: {theme['accent_color']};
                color: {theme['selected_text_color']};
                padding: 10px 20px;
                font: {theme['font_size_medium']} "{theme['font_family']}";
                border-radius: 5px;
                min-width: 100px;
            }}
            QMessageBox QPushButton:hover {{
                background-color: {theme['accent_hover']};
            }}
            QMessageBox QPushButton:pressed {{
                background-color: {theme['accent_pressed']};
            }}
        """
        msg_box.setStyleSheet(stylesheet)
        msg_box.exec()

   