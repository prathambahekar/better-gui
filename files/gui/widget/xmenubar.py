from PyQt6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, pyqtSignal

class xMenuBar(QMenuBar):
    """
    A custom menu bar widget for PyQt6 applications, styled with a theme and supporting dynamic menu actions.
    
    Args:
        theme (dict): A dictionary containing theme properties (e.g., colors, fonts).
        parent (QWidget, optional): The parent widget. Defaults to None.
    """
    
    # Custom signals for menu actions (can be connected in the parent)
    fileNewTriggered = pyqtSignal()
    fileOpenTriggered = pyqtSignal()
    fileSaveTriggered = pyqtSignal()
    editCutTriggered = pyqtSignal()
    editCopyTriggered = pyqtSignal()
    editPasteTriggered = pyqtSignal()
    viewZoomInTriggered = pyqtSignal()
    viewZoomOutTriggered = pyqtSignal()

    def __init__(self, theme, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.init_ui()

    def init_ui(self):
        """Initialize the menu bar UI, including styling and menu structure."""
        # Apply custom styling
        self._apply_stylesheet()
        
        # Create and configure menus
        self._create_menus()
        
    def _apply_stylesheet(self):
        """Apply the theme-based stylesheet for the menu bar and its components."""
        self.setStyleSheet(f"""
            QMenuBar {{
                background-color: transparent;
                color: {self.theme['text_color']};
                font: {self.theme['font_size_medium']} "{self.theme['font_family']}";
                padding: 5px;
                border: none;
            }}
            QMenuBar::item {{
                padding: 5px 15px;
                margin: 0 2px;
                background-color: transparent;
                border-radius: 5px;
            }}
            QMenuBar::item:selected, QMenuBar::item:hover {{
                background-color: {self.theme['def_bg']};
                color: {self.theme['text_color']};
            }}
            QMenu {{
                background-color: {self.theme['secondary_bg']};
                color: {self.theme['text_color']};
                font: {self.theme['font_size_medium']} "{self.theme['font_family']}";
                border: 2px solid {self.theme['def_bg']};
                padding: 5px;
                border-radius: 5px;
            }}
            QMenu::item {{
                padding: 5px 20px;
                margin: 2px 0;
                border-radius: 5px;
            }}
            QMenu::item:selected, QMenu::item:hover {{
                background-color: {self.theme['accent_hover']};
                color: {self.theme['selected_text_color']};
            }}
            QMenu::separator {{
                height: 1px;
                background-color: {self.theme['accent_color']};
                margin: 2px 0;
            }}
        """)

    def _create_menus(self):
        """Create and configure the menu structure with actions and connections."""
        # File Menu
        file_menu = self.addMenu("File")
        self._add_file_actions(file_menu)

        # Edit Menu
        edit_menu = self.addMenu("Edit")
        self._add_edit_actions(edit_menu)

        # View Menu
        view_menu = self.addMenu("View")
        self._add_view_actions(view_menu)

    def _add_file_actions(self, menu):
        """Add actions to the File menu."""
        new_action = QAction(QIcon("path/to/new_icon.png"), "New", self)  # Optional icon
        new_action.triggered.connect(self.fileNewTriggered)
        menu.addAction(new_action)

        open_action = QAction(QIcon("path/to/open_icon.png"), "Open", self)
        open_action.triggered.connect(self.fileOpenTriggered)
        menu.addAction(open_action)

        save_action = QAction(QIcon("path/to/save_icon.png"), "Save", self)
        save_action.triggered.connect(self.fileSaveTriggered)
        menu.addAction(save_action)

        # Optional: Add a separator and exit action
        menu.addSeparator()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)

    def _add_edit_actions(self, menu):
        """Add actions to the Edit menu."""
        cut_action = QAction(QIcon("path/to/cut_icon.png"), "Cut", self)
        cut_action.triggered.connect(self.editCutTriggered)
        menu.addAction(cut_action)

        copy_action = QAction(QIcon("path/to/copy_icon.png"), "Copy", self)
        copy_action.triggered.connect(self.editCopyTriggered)
        menu.addAction(copy_action)

        paste_action = QAction(QIcon("path/to/paste_icon.png"), "Paste", self)
        paste_action.triggered.connect(self.editPasteTriggered)
        menu.addAction(paste_action)

    def _add_view_actions(self, menu):
        """Add actions to the View menu."""
        zoom_in_action = QAction(QIcon("path/to/zoom_in_icon.png"), "Zoom In", self)
        zoom_in_action.triggered.connect(self.viewZoomInTriggered)
        menu.addAction(zoom_in_action)

        zoom_out_action = QAction(QIcon("path/to/zoom_out_icon.png"), "Zoom Out", self)
        zoom_out_action.triggered.connect(self.viewZoomOutTriggered)
        menu.addAction(zoom_out_action)

    def update_theme(self, new_theme):
        """Update the theme and reapply the stylesheet."""
        self.theme = new_theme
        self._apply_stylesheet()

    def close(self):
        """Override close to emit a signal or handle cleanup if needed."""
        if self.parent():
            self.parent().close()

# # Example usage (optional, for testing):
# if __name__ == "__main__":
#     from PyQt6.QtWidgets import QApplication
#     import sys

#     app = QApplication(sys.argv)
    
#     # Sample theme dictionary
#     theme = {
#         'bg_color': '#2d2d2d',
#         'text_color': '#ffffff',
#         'accent_color': '#4a90e2',
#         'accent_hover': '#5ba4f3',
#         'accent_pressed': '#3a80d2',
#         'selected_text_color': '#ffffff',
#         'font_family': 'Arial',
#         'font_size_medium': '12px'
#     }
    
#     window = QMainWindow()
#     menu_bar = xMenuBar(theme)
#     window.setMenuBar(menu_bar)
#     window.setGeometry(100, 100, 800, 600)
#     window.show()
#     sys.exit(app.exec())