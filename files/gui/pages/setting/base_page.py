from PyQt6.QtWidgets import QWidget
from files.gui.pages.setting.clickable_frame import validate_theme, DEFAULT_THEME

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
            background-color: {self.current_theme['def_bg']};
            color: {self.current_theme['text_color']};
            font-size: {self.current_theme['font_size_title']};
        """)

    def reset_settings(self):
        """To be implemented by subclasses."""
        pass