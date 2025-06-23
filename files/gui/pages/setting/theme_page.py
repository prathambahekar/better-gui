from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QComboBox, QSlider, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from files.gui.pages.setting.settings_base import BaseSettingsPage, validate_theme, DEFAULT_THEME
from files.gui.widget.xlabel import xLabel
from files.gui.widget.xcombobox import xComboBox
from files.gui.widget.xslider import xSlider

class ThemeSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the Theme settings page."""
        layout = QVBoxLayout(self)
        layout.setSpacing(28)
        layout.setContentsMargins(32, 32, 32, 32)

        # Section title (sync with General page)
        FONT_FAMILY = "'Segoe UI Variable', 'Segoe UI', 'Inter', Arial, sans-serif"
        title_label = xLabel("Theme Settings", self.current_theme, self)
        title_label.setStyleSheet(f"""
            font-family: {FONT_FAMILY};
            font-size: 16pt;
            color: {self.current_theme['text_color']};
            padding: 10px;
        """)
        layout.addWidget(title_label)

        self.theme_selector = self.create_theme_selector()
        self.font_size_selector = self.create_font_size_selector()
        layout.addWidget(self.theme_selector)
        layout.addWidget(self.font_size_selector)
        layout.addStretch()

    def create_theme_selector(self):
        """Create theme selection widget."""
        frame = self.create_styled_frame()
        layout = QHBoxLayout(frame)

        label = xLabel("Theme:", self.current_theme, self)
        label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.combo = xComboBox(self.current_theme, self)
        self.combo.addItems(["Light", "Dark", "Custom"])
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
                background-color: {self.current_theme['hover_bg']};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
        """)
        # TODO: Connect to theme change logic if needed
        # self.combo.currentTextChanged.connect(self.parent().change_theme)

        layout.addWidget(label)
        layout.addWidget(self.combo)
        return frame

    def create_font_size_selector(self):
        """Create font size adjustment widget."""
        frame = self.create_styled_frame(min_height=70, max_height=100)
        layout = QVBoxLayout(frame)

        label = xLabel("Font Size", self.current_theme, self)
        label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        slider_layout = QHBoxLayout()
        self.slider = xSlider(self.current_theme, self)
        self.slider.setMinimum(8)
        self.slider.setMaximum(24)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.font_size_changed)

        self.size_label = xLabel("10 pt", self.current_theme, self)
        self.size_label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.size_label)

        layout.addWidget(label)
        layout.addLayout(slider_layout)
        return frame

    def create_styled_frame(self, min_height=50, max_height=80):
        """Create a styled frame with customizable height."""
        frame = QFrame(self)
        frame.setStyleSheet(f"""
            background-color: {self.current_theme['def_bg']};
            border-radius: 8px;
            padding: 5px;
        """)
        frame.setMinimumHeight(min_height)
        frame.setMaximumHeight(max_height)
        return frame

    def font_size_changed(self, value):
        """Handle font size change event."""
        self.current_theme['font_size_title'] = f"{value}pt"
        self.size_label.setText(f"{value} pt")
        # TODO: Call theme update logic if needed
        # self.parent().apply_theme(self.current_theme)

    def reset_settings(self):
        """Reset theme settings to default."""
        self.combo.setCurrentText("Dark")
        self.slider.setValue(10)
        self.size_label.setText("10 pt")

    def apply_theme(self, theme):
        """Apply the theme to the page."""
        super().apply_theme(theme)
        # Update widget stylesheets
        for widget in [self.theme_selector, self.font_size_selector]:
            for child in widget.findChildren((QLabel, QComboBox, xComboBox, xSlider)):
                if isinstance(child, QLabel):
                    child.setStyleSheet(f"""
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                    """)
                elif isinstance(child, xComboBox):
                    child.update_theme(self.current_theme)
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
                            background-color: {self.current_theme['hover_bg']};
                        }}
                        QComboBox::drop-down {{
                            border: none;
                        }}
                    """)
                elif isinstance(child, xSlider):
                    child.update_theme(self.current_theme)
        # Update size label
        if hasattr(self, 'size_label'):
            self.size_label.setStyleSheet(f"""
                color: {self.current_theme['text_color']};
                font-size: {self.current_theme['font_size_title']};
            """)