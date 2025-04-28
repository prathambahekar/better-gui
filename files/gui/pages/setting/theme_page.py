from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QComboBox, QSlider, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from files.gui.pages.setting.base_page import BaseSettingsPage

class ThemeSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the Theme settings page."""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Back button
        back_button = QPushButton("Back", self)
        back_button.setStyleSheet(f"""
            QPushButton {{
                background-color: #2c2c2c;
                color: {self.current_theme['text_color']};
                border: 1px solid #3c3c3c;
                border-radius: 7px;
                padding: 5px;
                font-size: {self.current_theme['font_size_title']};
            }}
            QPushButton:hover {{
                background-color: #3c3c3c;
            }}
        """)
        back_button.clicked.connect(self.parent().show_main_page)
        layout.addWidget(back_button)

        self.theme_selector = self.create_theme_selector()
        self.font_size_selector = self.create_font_size_selector()
        layout.addWidget(self.theme_selector)
        layout.addWidget(self.font_size_selector)
        layout.addStretch()

    def create_theme_selector(self):
        """Create theme selection widget."""
        frame = self.create_styled_frame()
        layout = QHBoxLayout(frame)

        label = QLabel("Theme:", self)
        label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.combo = QComboBox(self)
        self.combo.addItems(["Light", "Dark", "Custom"])
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: #2c2c2c;
                color: {self.current_theme['text_color']};
                border: 1px solid #3c3c3c;
                border-radius: 5px;
                padding: 5px;
                font-size: {self.current_theme['font_size_title']};
            }}
            QComboBox:hover {{
                background-color: #3c3c3c;
            }}
            QComboBox::drop-down {{
                border: none;
            }}
        """)
        self.combo.currentTextChanged.connect(self.parent().change_theme)

        layout.addWidget(label)
        layout.addWidget(self.combo)
        return frame

    def create_font_size_selector(self):
        """Create font size adjustment widget."""
        frame = self.create_styled_frame(min_height=70, max_height=100)
        layout = QVBoxLayout(frame)

        label = QLabel("Font Size", self)
        label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        slider_layout = QHBoxLayout()
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(8)
        self.slider.setMaximum(24)
        self.slider.setValue(10)
        self.slider.setStyleSheet(f"""
            QSlider {{
                background-color: transparent;
                color: {self.current_theme['text_color']};
            }}
            QSlider::groove:horizontal {{
                height: 6px;
                background: #3c3c3c;
                border-radius: 3px;
            }}
            QSlider::handle:horizontal {{
                background: #5c5c5c;
                border: 1px solid #4c4c4c;
                width: 12px;
                height: 12px;
                border-radius: 6px;
                margin: -3px 0;
            }}
            QSlider::handle:horizontal:hover {{
                background: #6c6c6c;
            }}
        """)
        self.slider.valueChanged.connect(self.font_size_changed)

        self.size_label = QLabel("10 pt", self)
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
        frame.setStyleSheet("""
            background-color: #2c2c2c;
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
        self.parent().apply_theme(self.current_theme)

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
            for child in widget.findChildren((QLabel, QComboBox, QSlider)):
                if isinstance(child, QLabel):
                    child.setStyleSheet(f"""
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                    """)
                elif isinstance(child, QComboBox):
                    child.setStyleSheet(f"""
                        QComboBox {{
                            background-color: #2c2c2c;
                            color: {self.current_theme['text_color']};
                            border: 1px solid #3c3c3c;
                            border-radius: 5px;
                            padding: 5px;
                            font-size: {self.current_theme['font_size_title']};
                        }}
                        QComboBox:hover {{
                            background-color: #3c3c3c;
                        }}
                        QComboBox::drop-down {{
                            border: none;
                        }}
                    """)
                elif isinstance(child, QSlider):
                    child.setStyleSheet(f"""
                        QSlider {{
                            background-color: transparent;
                            color: {self.current_theme['text_color']};
                        }}
                        QSlider::groove:horizontal {{
                            height: 6px;
                            background: #3c3c3c;
                            border-radius: 3px;
                        }}
                        QSlider::handle:horizontal {{
                            background: #5c5c5c;
                            border: 1px solid #4c4c4c;
                            width: 12px;
                            height: 12px;
                            border-radius: 6px;
                            margin: -3px 0;
                        }}
                        QSlider::handle:horizontal:hover {{
                            background: #6c6c6c;
                        }}
                    """)
        # Update size label
        if hasattr(self, 'size_label'):
            self.size_label.setStyleSheet(f"""
                color: {self.current_theme['text_color']};
                font-size: {self.current_theme['font_size_title']};
            """)
        # Update back button
        back_button = self.findChild(QPushButton)
        if back_button:
            back_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: #2c2c2c;
                    color: {self.current_theme['text_color']};
                    border: 1px solid #3c3c3c;
                    border-radius: 7px;
                    padding: 5px;
                    font-size: {self.current_theme['font_size_title']};
                }}
                QPushButton:hover {{
                    background-color: #3c3c3c;
                }}
            """)