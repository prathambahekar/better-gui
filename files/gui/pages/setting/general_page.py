from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from files.gui.pages.setting.settings_base import BaseSettingsPage, validate_theme, DEFAULT_THEME
from files.gui.widget.xlabel import xLabel
from files.gui.widget.xcombobox import xComboBox
from files.gui.widget.xcheckbox import xCheckBox

ACCENT_COLOR = "#2563eb"  # Windows 11 accent blue
FONT_FAMILY = "'Segoe UI Variable', 'Segoe UI', 'Inter', Arial, sans-serif"

class GeneralSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the General settings page."""
        layout = QVBoxLayout(self)
        layout.setSpacing(28)
        layout.setContentsMargins(32, 32, 32, 32)

        # Section title
        title_label = xLabel("General Settings", self.current_theme, self)
        title_label.setStyleSheet(f"""
            font-family: {FONT_FAMILY};
            font-size: 16pt;
            color: {self.current_theme['text_color']};
            padding: 10px;
            
        """)
        layout.addWidget(title_label)

        self.language_selector = self.create_language_selector()
        layout.addWidget(self.language_selector)
        layout.addStretch()

    def create_language_selector(self):
        """Create language selection widget."""
        frame = QFrame(self)
        frame.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
            padding: 14px 28px;
        """)
        frame.setMinimumHeight(56)
        frame.setMaximumHeight(90)
        layout = QHBoxLayout(frame)
        layout.setSpacing(18)

        label = xLabel("Language:", self.current_theme, self)
        label.setStyleSheet(f"""
            font-family: {FONT_FAMILY};
            color: {self.current_theme['text_color']};
            font-size: 13pt;
            font-weight: 500;
        """)
        combo = xComboBox(self.current_theme, self)
        combo.addItems(["English", "Spanish", "French"])
        combo.currentTextChanged.connect(self.language_changed)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(combo)
        return frame

    def create_styled_frame(self):
        """Create a styled frame for consistent appearance."""
        frame = QFrame(self)
        frame.setStyleSheet("""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
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
        # No self.combo or checkbox, so no reset needed

    def apply_theme(self, theme):
        """Apply the theme to the page."""
        super().apply_theme(theme)
        # Update widget stylesheets
        self.language_selector.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
        """)
        # No notifications_toggle or checkbox to style
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