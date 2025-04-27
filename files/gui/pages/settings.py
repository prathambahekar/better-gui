from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QSlider, QCheckBox, QStackedWidget,
    QLabel, QPushButton, QTextBrowser, QScrollArea, QComboBox
)
from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtGui import QColor, QPalette, QFont, QPixmap, QPainter, QDesktopServices
from PyQt6.QtSvg import QSvgRenderer
import os
import uuid

# Default theme to ensure robustness
DEFAULT_THEME = {
    'secondary_bg': '#1e1e1e',
    'text_color': '#ffffff',
    'font_family': 'Segoe UI Variable',
    'font_size_title': '10pt'
}

def validate_theme(theme):
    """Ensure the theme dictionary has all required keys."""
    validated = DEFAULT_THEME.copy()
    validated.update(theme)
    return validated

class ClickableFrame(QFrame):
    """A QFrame subclass that emits a signal when clicked, with SVG icon on left, text in center, and '>' on right."""
    clicked = pyqtSignal()

    def __init__(self, text="", icon_path=None, parent=None, theme=DEFAULT_THEME):
        super().__init__(parent)
        self.theme = validate_theme(theme)
        self.setMouseTracking(True)

        # Set the stylesheet for the frame and labels
        self.setStyleSheet(f"""
            QFrame {{
                background-color: #2c2c2c;
                border-radius: 7px;
                padding: 0px;
            }}
            QFrame:hover {{
                background-color: #3c3c3c;
            }}
            QLabel {{
                background-color: transparent;
                color: {self.theme['text_color']};
                font-size: {self.theme['font_size_title']};
            }}
            QLabel#rightArrow {{
                font-size: 16px;
                font-weight: bold;
                color: #cccccc;
            }}
            QLabel#iconLabel {{
                background-color: transparent;
            }}
        """)

        # Set size constraints
        self.setMinimumHeight(70)
        self.setMaximumHeight(80)

        # Create layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(10)

        # Left SVG icon
        icon_label = QLabel(self)
        icon_label.setObjectName("iconLabel")
        # Use a default icon path if none provided
        if not icon_path:
            icon_path = os.path.join('files', 'gui', 'icons', 'settings.svg')
        if icon_path and icon_path.lower().endswith('.svg') and os.path.exists(icon_path):
            renderer = QSvgRenderer(icon_path)
            if renderer.isValid():
                pixmap = QPixmap(24, 24)
                pixmap.fill(Qt.GlobalColor.transparent)
                painter = QPainter(pixmap)
                renderer.render(painter)
                painter.end()
                icon_label.setPixmap(pixmap)
            else:
                icon_label.setText("Icon")  # Fallback
        else:
            icon_label.setText("Icon")  # Fallback
        icon_label.setFixedWidth(30)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(icon_label)

        # Center text
        text = str(text)
        text_label = QLabel(text, self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont(self.theme['font_family'], 10))
        layout.addWidget(text_label, stretch=1)

        # Right arrow
        right_arrow = QLabel(">", self)
        right_arrow.setObjectName("rightArrow")
        right_arrow.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(right_arrow)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        """Emit the clicked signal when the frame is clicked."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

    def apply_theme(self, theme):
        """Update the theme for the frame."""
        self.theme = validate_theme(theme)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: #2c2c2c;
                border-radius: 7px;
                padding: 0px;
            }}
            QFrame:hover {{
                background-color: #3c3c3c;
            }}
            QLabel {{
                background-color: transparent;
                color: {self.theme['text_color']};
                font-size: {self.theme['font_size_title']};
            }}
            QLabel#rightArrow {{
                font-size: 18px;
                font-weight: bold;
                color: #cccccc;
            }}
            QLabel#iconLabel {{
                background-color: transparent;
            }}
        """)

class SettingsPage(QWidget):
    theme_changed = pyqtSignal(str)

    def __init__(self, parent=None, theme=DEFAULT_THEME):
        super().__init__(parent)
        self.parent_widget = parent
        self.current_theme = validate_theme(theme)
        self.navigation_path = ["Personalization"]
        self.setup_ui()

    def setup_ui(self):
        """Initialize the main layout and components."""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Location bar
        self.location_bar = QLabel("Personalization", self)
        self.location_bar.setStyleSheet(f"""
            font-weight: bold;
            padding: 5px;
            background-color: {self.current_theme['secondary_bg']};
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.location_bar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.location_bar.mousePressEvent = lambda event: self.show_main_page()
        main_layout.addWidget(self.location_bar)

        # Stacked widget to switch between main page and sub-pages
        self.stacked_widget = QStackedWidget(self)

        # Create main page with clickable frames
        self.main_page = self.create_main_page()

        # Create sub-pages
        self.pages = {
            "General": GeneralSettingsPage(self, self.current_theme),
            "Theme": ThemeSettingsPage(self, self.current_theme),
            "About": AboutSettingsPage(self, self.current_theme)
        }

        # Add main page and sub-pages to stacked widget
        self.stacked_widget.addWidget(self.main_page)
        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        main_layout.addWidget(self.stacked_widget)
        self.apply_theme(self.current_theme)

    def create_main_page(self):
        """Create the main page with clickable frames for navigation."""
        main_page = QWidget(self)
        layout = QVBoxLayout(main_page)
        layout.setSpacing(10)

        nav_items = [
            ("General Settings", self.show_general_page),
            ("Theme Settings", self.show_theme_page),
            ("About", self.show_about_page)
        ]

        for text, handler in nav_items:
            frame = ClickableFrame(text, theme=self.current_theme, parent=main_page)
            frame.clicked.connect(handler)
            layout.addWidget(frame)

        layout.addStretch()
        return main_page

    def show_general_page(self):
        """Switch to the General settings page."""
        self.stacked_widget.setCurrentWidget(self.pages["General"])
        self.navigation_path = ["Personalization", "General"]
        self.update_location_bar()

    def show_theme_page(self):
        """Switch to the Theme settings page."""
        self.stacked_widget.setCurrentWidget(self.pages["Theme"])
        self.navigation_path = ["Personalization", "Theme"]
        self.update_location_bar()

    def show_about_page(self):
        """Switch to the About settings page."""
        self.stacked_widget.setCurrentWidget(self.pages["About"])
        self.navigation_path = ["Personalization", "About"]
        self.update_location_bar()

    def show_main_page(self):
        """Switch back to the main page."""
        self.stacked_widget.setCurrentWidget(self.main_page)
        self.navigation_path = ["Personalization"]
        self.update_location_bar()

    def update_location_bar(self):
        """Update the location bar text based on the current navigation path."""
        self.location_bar.setText(" > ".join(self.navigation_path))

    def apply_theme(self, theme):
        """Apply the selected theme to the settings page."""
        self.current_theme = validate_theme(theme)
        self.setStyleSheet(f"""
            background-color: {self.current_theme['secondary_bg']};
            color: {self.current_theme['text_color']};
            font-family: {self.current_theme['font_family']};
            font-size: {self.current_theme['font_size_title']};
        """)
        self.location_bar.setStyleSheet(f"""
            font-weight: bold;
            padding: 5px;
            background-color: {self.current_theme['secondary_bg']};
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)
        for frame in self.main_page.findChildren(ClickableFrame):
            frame.apply_theme(self.current_theme)
        for page in self.pages.values():
            page.apply_theme(self.current_theme)

    def change_theme(self, theme_name):
        """Handle theme change and emit signal."""
        # Update theme based on theme_name
        theme_map = {
            "Light": {
                'secondary_bg': '#f0f0f0',
                'text_color': '#000000',
                'font_family': 'Arial',
                'font_size_title': '10pt'
            },
            "Dark": DEFAULT_THEME,
            "Custom": {
                'secondary_bg': '#2e2e2e',
                'text_color': '#dddddd',
                'font_family': 'Arial',
                'font_size_title': '10pt'
            }
        }
        new_theme = validate_theme(theme_map.get(theme_name, DEFAULT_THEME))
        self.apply_theme(new_theme)
        self.theme_changed.emit(theme_name)

    def reset_settings(self):
        """Reset all settings to default values."""
        self.current_theme = DEFAULT_THEME
        self.apply_theme(self.current_theme)
        self.theme_changed.emit("Dark")
        self.pages["General"].reset_settings()
        self.pages["Theme"].reset_settings()

class BaseSettingsPage(QWidget):
    """Base class for settings pages to enforce common behavior."""
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.current_theme = validate_theme(theme)
        self.setup_ui()

    def setup_ui(self):
        """To be implemented by subclasses."""
        pass

    def apply_theme(self, theme):
        """Apply the theme to the page."""
        self.current_theme = validate_theme(theme)
        self.setStyleSheet(f"""
            background-color: {self.current_theme['secondary_bg']};
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)

    def reset_settings(self):
        """To be implemented by subclasses."""
        pass

class GeneralSettingsPage(BaseSettingsPage):
    def setup_ui(self):
        """Set up the General settings page."""
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
            background-color: #2c2c2c;
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