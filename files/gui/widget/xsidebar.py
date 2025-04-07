from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation
from PyQt6.QtGui import QIcon
import files.app.config as config
import darkdetect

class SidebarButton(QPushButton):
    """
    A custom push button for the sidebar, supporting expanded and collapsed states with SVG icons.
    """
    def __init__(self, icon=None, expanded_icon=None, full_text=None, is_toggle=False, theme=None, parent=None):
        """
        Initialize the sidebar button.
        """
        super().__init__(parent)
        self.icon = icon
        self.expanded_icon = expanded_icon
        self.full_text = full_text
        self.is_toggle = is_toggle
        self.theme = theme if theme else {}
        self.update_theme_colors()
        self.setIconSize(QSize(26, 26))  # Consistent icon size
        self.apply_style()  # Apply style with centered icon by default
        self.set_expanded(False)  # Initially collapsed

    def update_theme_colors(self):
        """Update theme colors based on dark/light mode."""
        self.theme['button_bg'] = config.STYLE_CONFIG_DARK["bg_color"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["bg_color"]
        self.theme['text_color'] = config.STYLE_CONFIG_LIGHT["selected_text_color"] if darkdetect.isDark() else config.STYLE_CONFIG_DARK["selected_text_color"]
        self.theme['button_hover'] = config.STYLE_CONFIG_DARK["def_bg"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["def_bg"]
        self.theme['button_pressed'] = config.STYLE_CONFIG_DARK["secondary_bg"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["secondary_bg"]
        self.theme['font_family'] = config.STYLE_CONFIG_DARK["font_family"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["font_family"]
        self.theme['font_size_medium'] = config.STYLE_CONFIG_DARK["font_size_medium"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["font_size_medium"]

    def apply_style(self, text_left=False):
        """Apply stylesheet based on the current theme, with centered icon by default."""
        alignment = "left" if text_left else "center"
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.theme.get('button_bg', 'transparent')};
                color: {self.theme.get('text_color', '#000000')};
                border: none;
                border-radius: 5px;
                padding: 5px;
                font: {self.theme['font_size_medium']} "{self.theme['font_family']}";
                margin: 2px;
                text-align: {alignment};
            }}
            QPushButton:hover {{
                background-color: {self.theme.get('button_hover', '#2d2d2d')};
            }}
            QPushButton:pressed {{
                background-color: {self.theme.get('button_pressed', 'rgba(0, 0, 0, 60)')};
            }}
        """)

    def update_theme(self, new_theme):
        """Update the button's theme and reapply styles."""
        self.theme = new_theme
        self.update_theme_colors()
        self.apply_style()

    def set_expanded(self, expanded):
        """
        Set the button's icon and text based on the expanded state.
        """
        if self.is_toggle:
            self.setIcon(self.expanded_icon if expanded else self.icon)
            self.setText("")  # Toggle button uses icon only
            self.apply_style(text_left=False)  # Keep icon centered
        else:
            self.setIcon(self.icon)
            self.setText(self.full_text if expanded else "")
            self.apply_style(text_left=expanded)  # Left-align only when text is present

class xSidebar(QFrame):
    """
    A collapsible sidebar with dynamically added buttons using SVG icons.
    Supports theming based on dark/light mode and top/bottom button placement.
    """
    def __init__(self, parent=None, theme=None):
        """
        Initialize the sidebar.

        Parameters:
        - parent (QWidget): Parent widget.
        - theme (dict): Theme configuration for styling.
        """
        super().__init__(parent)
        self.theme = theme if theme is not None else {}
        self.update_theme_colors()
        self.is_expanded = False
        self.min_width = 50
        self.max_width = 250
        self.setMinimumWidth(self.min_width)
        self.setMaximumWidth(self.max_width)
        self.setup_ui()
        self.apply_theme()

    def update_theme_colors(self):
        """Update theme colors based on dark/light mode."""
        self.theme['bg_color'] = config.STYLE_CONFIG_DARK["bg_color"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["bg_color"]
        self.theme['text_color'] = config.STYLE_CONFIG_DARK["selected_text_color"] if darkdetect.isDark() else config.STYLE_CONFIG_LIGHT["selected_text_color"]
        # Optional: Define separator color in theme
        self.theme['separator_color'] = '#555555' if darkdetect.isDark() else '#cccccc'

    def setup_ui(self):
        """Set up the sidebar's UI with a toggle button and dynamic buttons."""
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Create toggle button
        self.toggle_btn = SidebarButton(
            icon=QIcon("files\\gui\\icons\\menu.svg"),           # Placeholder for hamburger icon
            expanded_icon=QIcon("files\\gui\\icons\\menu.svg"), # Placeholder for close icon
            is_toggle=True,
            theme=self.theme,
            parent=self
        )
        self.toggle_btn.setFixedHeight(50)

        # Define button configurations with position option
        self.button_configs = [
            {"name": "home", "icon": QIcon("files\\gui\\icons\\home.svg"), "full_text": "Home", "position": "top"},
            {"name": "settings", "icon": QIcon("files\\gui\\icons\\settings.svg"), "full_text": "Settings", "position": "bottom"},
            # Add more buttons as needed, e.g.,
            # {"name": "about", "icon": QIcon("files\\gui\\icons\\about.svg"), "full_text": "About", "position": "top"},
        ]

        # Create and store buttons dynamically
        self.buttons = {}
        top_buttons = []
        bottom_buttons = []

        for config in self.button_configs:
            btn = SidebarButton(
                icon=config["icon"],
                full_text=config["full_text"],
                theme=self.theme,
                parent=self
            )
            btn.setFixedHeight(50)
            self.buttons[config["name"]] = btn
            if config.get("position", "top") == "top":
                top_buttons.append(btn)
            else:
                bottom_buttons.append(btn)

        # Add widgets to the layout
        self.layout.addWidget(self.toggle_btn)
        for btn in top_buttons:
            self.layout.addWidget(btn)
        self.layout.addStretch()  # Push bottom content down

        if bottom_buttons:
            # # Create and add separator
            # self.separator = QFrame()
            # self.separator.setFrameShape(QFrame.Shape.HLine)  # Fixed previously
            # self.separator.setFrameShadow(QFrame.Shadow.Sunken)  # Fixed: Use QFrame.Shadow.Sunken
            # self.separator.setFixedHeight(1)
            # self.layout.addWidget(self.separator)
            # Add bottom buttons
            for btn in bottom_buttons:
                self.layout.addWidget(btn)

        # Connect toggle button
        self.toggle_btn.clicked.connect(self.toggle_sidebar)

    def apply_theme(self):
        """Apply stylesheet to the sidebar and update button themes."""
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {self.theme.get('bg_color', 'rgba(243, 243, 243, 180)')};
                border: none;
                border-radius: 7px;
            }}
        """)
        for btn in [self.toggle_btn] + list(self.buttons.values()):
            btn.update_theme(self.theme)
        if hasattr(self, 'separator') and self.separator:
            self.separator.setStyleSheet(f"background-color: {self.theme.get('separator_color', '#cccccc')};")

    def toggle_sidebar(self):
        """Toggle the sidebar between collapsed and expanded states."""
        present_width = self.width()
        start_width = present_width
        end_width = self.max_width if not self.is_expanded else self.min_width

        # Create animation for smooth width transition
        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(end_width)

        # Update all buttons based on new state
        expanded = not self.is_expanded
        self.toggle_btn.set_expanded(expanded)
        for btn in self.buttons.values():
            btn.set_expanded(expanded)

        # Start animation and update state
        self.animation.start()
        self.is_expanded = expanded

# Example usage (optional, for testing):
# if __name__ == "__main__":
#     app = QApplication([])
#     window = QMainWindow()
#     sidebar = xSidebar(window)
#     window.setCentralWidget(QWidget())  # Placeholder central widget
#     window.resize(800, 600)
#     sidebar.show()
#     app.exec()