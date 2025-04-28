from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget, QLabel
)
from PyQt6.QtCore import Qt, pyqtSignal
from files.gui.pages.setting.clickable_frame import ClickableFrame, validate_theme, DEFAULT_THEME
from files.gui.pages.setting.general_settings_page import GeneralSettingsPage
from files.gui.pages.setting.theme_settings_page import ThemeSettingsPage
from files.gui.pages.setting.about_settings_page import AboutSettingsPage

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
        self.main_page = self.create_main_page()  # Correct assignment

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