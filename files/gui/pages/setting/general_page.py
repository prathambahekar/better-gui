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
        self.notifications_toggle = self.create_notifications_toggle()
        layout.addWidget(self.language_selector)
        layout.addWidget(self.notifications_toggle)
        layout.addStretch()

    def create_language_selector(self):
        """Create language selection widget."""
        frame = QFrame(self)
        frame.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
            padding: 18px 24px;
        """)
        frame.setMinimumHeight(56)
        frame.setMaximumHeight(90)
        layout = QHBoxLayout(frame)
        layout.setSpacing(18)

        label = xLabel("Language:", self.current_theme, self)
        label.setStyleSheet(f"""
            font-family: {FONT_FAMILY};
            color: {self.current_theme['text_color']};
            font-size: 11.5pt;
            font-weight: 500;
        """)
        self.combo = xComboBox(self.current_theme, self)
        self.combo.addItems(["English", "Spanish", "French"])
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: #f3f3f3;
                color: #222;
                border: 1px;
                border-radius: 7px;
                padding: 6px 12px;
                font-size: 11pt;
                font-family: {FONT_FAMILY};
                min-width: 120px;
            }}
            QComboBox:hover {{
                border: 1px solid #b0b0b0;
                background-color: #ededed;
            }}
            QComboBox:focus {{
                border: 1.5px solid {ACCENT_COLOR};
            }}
            QComboBox::drop-down {{
                border: none;
                background: transparent;
            }}
        """)
        self.combo.currentTextChanged.connect(self.language_changed)

        layout.addWidget(label)
        layout.addWidget(self.combo)
        layout.addStretch()
        return frame

    def create_notifications_toggle(self):
        """Create notifications toggle widget."""
        frame = QFrame(self)
        frame.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
            padding: 18px 24px;
        """)
        frame.setMinimumHeight(56)
        frame.setMaximumHeight(90)
        layout = QHBoxLayout(frame)
        layout.setSpacing(18)

        # Modern toggle switch using xCheckBox
        self.checkbox = xCheckBox("Enable Notifications", self.current_theme, self)
        self.checkbox.setChecked(True)
        layout.addWidget(self.checkbox)
        layout.addStretch()
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
        self.language_selector.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
            padding: 18px 24px;
        """)
        self.notifications_toggle.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 7px;
            padding: 18px 24px;
        """)
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: #f3f3f3;
                color: #222;
                border: 1px;
                border-radius: 7px;
                padding: 6px 12px;
                font-size: 11pt;
                font-family: {FONT_FAMILY};
                min-width: 120px;
            }}
            QComboBox:hover {{
                border: 1px solid #b0b0b0;
                background-color: #ededed;
            }}
            QComboBox:focus {{
                border: 1.5px solid {ACCENT_COLOR};
            }}
            QComboBox::drop-down {{
                border: none;
                background: transparent;
            }}
        """)
        self.checkbox.setStyleSheet(f"""
            QCheckBox {{
                font-family: {FONT_FAMILY};
                color: #222;
                font-size: 11.5pt;
                font-weight: 500;
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
                background: {ACCENT_COLOR};
                border: 1px solid {ACCENT_COLOR};
            }}
            QCheckBox::indicator:unchecked:pressed,
            QCheckBox::indicator:checked:pressed {{
                background: #a0a0a0;
            }}
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