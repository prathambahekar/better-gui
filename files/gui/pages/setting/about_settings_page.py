from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from files.gui.pages.setting.base_settings_page import BaseSettingsPage

class AboutSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the scrollable About settings page with improved stylesheet."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Create scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.update_scroll_area_stylesheet()
        # Create content widget for scroll area
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.setSpacing(10)
        self.content_layout.setContentsMargins(10, 10, 10, 10)

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
        self.content_layout.addWidget(back_button)

        # Application title
        app_title = QLabel("Application Settings", self)
        app_title.setStyleSheet(f"""
            font-size: 12pt;
            font-weight: bold;
            color: {self.current_theme['text_color']};
            padding: 5px;
        """)
        app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(app_title)

        # Application description
        app_description = """
        Application Settings is a customizable interface for managing user preferences.
        It offers theme selection, language options, and notification settings, designed
        for a seamless and intuitive user experience.
        """
        desc_label = QLabel(app_description.strip(), self)
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setStyleSheet(f"""
            background-color: #2c2c2c;
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
            border-radius: 7px;
            padding: 10px;
        """)
        self.content_layout.addWidget(desc_label)

        # Developer and version information
        dev_info = """
        <b>Developer:</b> Pratham Bahekar<br>
        <b>Version:</b> 1.0.0<br>
        <b>License:</b> DIT License
        """
        dev_label = QLabel(dev_info, self)
        dev_label.setTextFormat(Qt.TextFormat.RichText)
        dev_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dev_label.setStyleSheet(f"""
            background-color: #2c2c2c;
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
            border-radius: 7px;
            padding: 10px;
        """)
        self.content_layout.addWidget(dev_label)

        # Developer website link
        website_label = QLabel(
            '<a href="https://prathambahekar.dev" style="color: #1e90ff; text-decoration: none;">'
            'Visit Developer Website</a>',
            self
        )
        website_label.setTextFormat(Qt.TextFormat.RichText)
        website_label.setStyleSheet(f"""
            background-color: #2c2c2c;
            color: #1e90ff;
            font-size: {self.current_theme['font_size_title']};
            border-radius: 7px;
            padding: 5px;
        """)
        website_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        website_label.setFixedHeight(40)
        website_label.setCursor(Qt.CursorShape.PointingHandCursor)
        # Handle click to open URL
        def open_website(event):
            if event.button() == Qt.MouseButton.LeftButton:
                QDesktopServices.openUrl(QUrl("https://prathambahekar.dev"))
        website_label.mousePressEvent = open_website
        self.content_layout.addWidget(website_label)

        # Contact email button
        contact_button = QPushButton("Contact Developer", self)
        contact_button.setStyleSheet(f"""
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
        contact_button.clicked.connect(self.open_email_client)
        self.content_layout.addWidget(contact_button)

        # Check for updates button
        update_button = QPushButton("Check for Updates", self)
        update_button.setStyleSheet(f"""
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
        update_button.clicked.connect(self.check_for_updates)
        self.content_layout.addWidget(update_button)

        self.content_layout.addStretch()

        # Set the content widget to the scroll area
        self.scroll_area.setWidget(content_widget)
        main_layout.addWidget(self.scroll_area)

    def update_scroll_area_stylesheet(self):
        """Update the scroll area stylesheet based on the current theme."""
        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                background-color: {self.current_theme['secondary_bg']};
                border: none;
            }}
            QScrollBar:vertical {{
                border: none;
                background: #2c2c2c;
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: #3c3c3c;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: #4c4c4c;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                background: none;
            }}
        """)

    def open_email_client(self):
        """Open the default email client with a pre-filled email."""
        email = "mailto:contact@prathambahekar.dev?subject=Application%20Settings%20Feedback"
        QDesktopServices.openUrl(QUrl(email))

    def check_for_updates(self):
        """Simulate checking for updates."""
        # Remove any existing update message
        for i in range(self.content_layout.count()):
            widget = self.content_layout.itemAt(i).widget()
            if isinstance(widget, QLabel) and widget.text().startswith("No updates available"):
                self.content_layout.removeWidget(widget)
                widget.deleteLater()
                break

        update_message = QLabel("No updates available. You are using the latest version.", self)
        update_message.setStyleSheet(f"""
            background-color: #2c2c2c;
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
            border-radius: 7px;
            padding: 5px;
        """)
        update_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.insertWidget(self.content_layout.count() - 1, update_message)

    def apply_theme(self, theme):
        """Apply the theme to the page."""
        super().apply_theme(theme)
        self.update_scroll_area_stylesheet()
        # Update widget stylesheets
        for widget in self.findChildren((QLabel, QPushButton)):
            if isinstance(widget, QLabel):
                if widget.text().startswith("<a"):  # Website link
                    widget.setStyleSheet(f"""
                        background-color: #2c2c2c;
                        color: #1e90ff;
                        font-size: {self.current_theme['font_size_title']};
                        border-radius: 7px;
                        padding: 5px;
                    """)
                elif widget.text() == "Application Settings":  # Title
                    widget.setStyleSheet(f"""
                        font-size: 12pt;
                        font-weight: bold;
                        color: {self.current_theme['text_color']};
                        padding: 5px;
                    """)
                else:  # Other labels
                    widget.setStyleSheet(f"""
                        background-color: #2c2c2c;
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                        border-radius: 7px;
                        padding: 10px;
                    """)
            elif isinstance(widget, QPushButton):
                widget.setStyleSheet(f"""
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

    def reset_settings(self):
        """No settings to reset in About page."""
        pass