from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QComboBox, QCheckBox, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from files.gui.pages.setting.settings_base import BaseSettingsPage, validate_theme, DEFAULT_THEME

class GeneralSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the General settings page."""
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Section title
        title_label = QLabel("General Settings", self)
        title_label.setStyleSheet(f"""
            font-size: {self.current_theme['font_size_large']};
            font-weight: bold;
            color: {self.current_theme['text_color']};
            padding-bottom: 10px;
        """)
        layout.addWidget(title_label)

        self.language_selector = self.create_language_selector()
        self.notifications_toggle = self.create_notifications_toggle()
        layout.addWidget(self.language_selector)
        layout.addWidget(self.notifications_toggle)
        layout.addStretch()

    def create_language_selector(self):
        """Create language selection widget."""
        frame = self.create_styled_frame()
        layout = QHBoxLayout(frame)

        label = QLabel("Language:", self)
        label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.combo = QComboBox(self)
        self.combo.addItems(["English", "Spanish", "French"])
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {self.current_theme['def_bg']};
                color: {self.current_theme['text_color']};
                border: 1px solid {self.current_theme['border_color']};
                border-radius: 5px;
                padding: 5px;
                font-size: {self.current_theme['font_size_title']};
            }}
            QComboBox:hover {{
                background-color: {self.current_theme['secondary_bg']};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
        """)
        self.combo.currentTextChanged.connect(self.language_changed)

        layout.addWidget(label)
        layout.addWidget(self.combo)
        return frame

    def create_notifications_toggle(self):
        """Create notifications toggle widget."""
        frame = self.create_styled_frame()
        layout = QVBoxLayout(frame)

        self.checkbox = QCheckBox("Enable Notifications", self)
        self.checkbox.setChecked(True)
        self.checkbox.setStyleSheet(f"""
            QCheckBox {{
                color: {self.current_theme['text_color']};
                font-size: {self.current_theme['font_size_title']};
            }}
        """)
        layout.addWidget(self.checkbox)
        return frame

    def create_styled_frame(self):
        """Create a styled frame for consistent appearance."""
        frame = QFrame(self)
        frame.setStyleSheet("""
            background-color: {self.current_theme['def_bg']};
            border-radius: 8px;
            padding: 5px;
        """)
        frame.setMinimumHeight(50)
        frame.setMaximumHeight(80)
        return frame

    def language_changed(self, lang):
        """Handle language change event."""
        print(f"Language changed to: {lang}")

    def reset_settings(self):
        """Reset general settings to default."""
        self.combo.setCurrentText("English")
        self.checkbox.setChecked(True)

    def apply_theme(self, theme):
        """Apply the theme to the page."""
        super().apply_theme(theme)
        # Update widget stylesheets
        for widget in [self.language_selector, self.notifications_toggle]:
            for child in widget.findChildren((QLabel, QComboBox, QCheckBox)):
                if isinstance(child, QLabel):
                    child.setStyleSheet(f"""
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                    """)
                elif isinstance(child, QComboBox):
                    child.setStyleSheet(f"""
                        QComboBox {{
                            background-color: {self.current_theme['def_bg']};
                            color: {self.current_theme['text_color']};
                            border: 1px solid {self.current_theme['border_color']};
                            border-radius: 5px;
                            padding: 5px;
                            font-size: {self.current_theme['font_size_title']};
                        }}
                        QComboBox:hover {{
                            background-color: {self.current_theme['secondary_bg']};
                        }}
                        QComboBox::drop-down {{
                            border: none;
                        }}
                    """)
                elif isinstance(child, QCheckBox):
                    child.setStyleSheet(f"""
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                    """)
        # Update back button
        back_button = self.findChild(QPushButton)
        if back_button:
            back_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.current_theme['def_bg']};
                    color: {self.current_theme['text_color']};
                    border: 1px solid {self.current_theme['border_color']};
                    border-radius: 7px;
                    padding: 5px;
                    font-size: {self.current_theme['font_size_title']};
                }}
                QPushButton:hover {{
                    background-color: {self.current_theme['secondary_bg']};
                }}
            """)