from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel, QFrame
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from files.gui.pages.setting.settings_base import BaseSettingsPage, validate_theme, DEFAULT_THEME
from files.gui.widget.xlabel import xLabel
from files.gui.widget.xbutton import xButton

class AboutSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the scrollable About settings page with improved stylesheet and styled frames for each section."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 16, 8, 16)
        main_layout.setSpacing(12)

        # Create scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.update_scroll_area_stylesheet()
        # Create content widget for scroll area
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_layout.setSpacing(12)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        # Helper for styled frame
        def create_styled_frame(widget, min_height=44, max_height=300):
            frame = QFrame(self)
            frame.setStyleSheet(f"""
                background-color: {self.current_theme['def_bg']};
                border-radius: 7px;
                padding: 8px 16px;
            """)
            frame.setMinimumHeight(min_height)
            frame.setMaximumHeight(max_height)
            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(widget)
            return frame

        # Application title
        # app_title = xLabel("Application Settings", self.current_theme, self)
        # app_title.setStyleSheet(f"""
        #     font-size: 12pt;
        #     font-weight: bold;
        #     color: {self.current_theme['text_color']};
        #     padding: 2px;
        # """)
        # app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.content_layout.addWidget(create_styled_frame(app_title, min_height=44, max_height=60))

        # Application description
        app_description = """
        Application Settings is a customizable interface for managing user preferences.
        It offers theme selection, language options, and notification settings, designed
        for a seamless and intuitive user experience.
        """
        desc_label = xLabel(app_description.strip(), self.current_theme, self)
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_large']};
        """)
        self.content_layout.addWidget(create_styled_frame(desc_label, min_height=150, max_height=300))

        # Developer and version information
        dev_info = """
        <b>Developer:</b> Pratham Bahekar<br>
        <b>Version:</b> 1.0.0<br>
        """
        dev_label = xLabel(dev_info, self.current_theme, self)
        dev_label.setTextFormat(Qt.TextFormat.RichText)
        dev_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dev_label.setStyleSheet(f"""
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.content_layout.addWidget(create_styled_frame(dev_label, min_height=44, max_height=150))

        # Developer website link
        link_color = self.current_theme.get('link_color', '#1e90ff')
        website_label = xLabel(
            f'<a href="https://prathambahekar.dev" style="color: {link_color}; text-decoration: none;">'
            'Visit Developer Website</a>',
            self.current_theme, self
        )
        website_label.setTextFormat(Qt.TextFormat.RichText)
        website_label.setStyleSheet(f"""
            color: {link_color};
            font-size: {self.current_theme['font_size_title']};
        """)
        website_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        website_label.setFixedHeight(32)
        website_label.setCursor(Qt.CursorShape.PointingHandCursor)
        def open_website(event):
            if event.button() == Qt.MouseButton.LeftButton:
                QDesktopServices.openUrl(QUrl("https://prathambahekar.dev"))
        website_label.mousePressEvent = open_website
        self.content_layout.addWidget(create_styled_frame(website_label, min_height=44, max_height=60))

        # Contact email button
        contact_button = xButton("Contact Developer", self)
        contact_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.current_theme['def_bg']};
                color: {self.current_theme['text_color']};
                border: 1px;
                border-radius: 7px;
                font-size: {self.current_theme['font_size_title']};
            }}
            QPushButton:hover {{
                background-color: {self.current_theme['hover_bg']};
            }}
        """)
        contact_button.clicked.connect(self.open_email_client)
        self.content_layout.addWidget(create_styled_frame(contact_button, min_height=44, max_height=60))

        # Check for updates button
        update_button = xButton("Check for Updates", self)
        update_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.current_theme['def_bg']};
                color: {self.current_theme['text_color']};
                border: 1px;
                border-radius: 7px;
                font-size: {self.current_theme['font_size_title']};
            }}
            QPushButton:hover {{
                background-color: {self.current_theme['hover_bg']};
            }}
        """)
        update_button.clicked.connect(self.check_for_updates)
        self.content_layout.addWidget(create_styled_frame(update_button, min_height=44, max_height=60))

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
                background: {self.current_theme['secondary_bg']};
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {self.current_theme['border_color']};
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {self.current_theme['hover_bg']};
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
            background-color: {self.current_theme['def_bg']};
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
                    link_color = self.current_theme.get('link_color', '#1e90ff')
                    widget.setStyleSheet(f"""
                        background-color: {self.current_theme['def_bg']};
                        color: {link_color};
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
                        background-color: {self.current_theme['def_bg']};
                        color: {self.current_theme['text_color']};
                        font-size: {self.current_theme['font_size_title']};
                        border-radius: 7px;
                        padding: 10px;
                    """)
            elif isinstance(widget, QPushButton):
                widget.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {self.current_theme['def_bg']};
                        color: {self.current_theme['text_color']};
                        border: 1px solid {self.current_theme['border_color']};
                        border-radius: 7px;
                        padding: 5px;
                        font-size: {self.current_theme['font_size_title']};
                    }}
                    QPushButton:hover {{
                        background-color: {self.current_theme['hover_bg']};
                    }}
                """)

    def reset_settings(self):
        """No settings to reset in About page."""
        pass