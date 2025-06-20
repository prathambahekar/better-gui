# files/gui/home_page.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt6.QtCore import Qt
from files.gui.ui_components import *
from files.app.app_functions import *

class HomePage(QWidget):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.parent = parent  # Reference to MainWindow
        self.current_theme = theme
        self.item_path = None
        self.setup_ui()

    def setup_ui(self):
        central_layout = QVBoxLayout(self)
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setSpacing(10)

        # Top bar with title and theme toggle
        top_bar = QHBoxLayout()
        self.title_label = xLabel("Konichiwa", self.current_theme, self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_bar.addWidget(self.title_label)
        top_bar.addStretch()
        self.theme_toggle = xButton("Light", self)
        self.theme_toggle.setFixedWidth(100)
        self.theme_toggle.clicked.connect(self.parent.toggle_theme)  # Delegate to MainWindow
        top_bar.addWidget(self.theme_toggle)

        # Add the top bar first
        central_layout.addLayout(top_bar)

        # Add vertical stretch to push the content above to the top
        central_layout.addStretch()


    def apply_theme(self, theme):
        self.current_theme = theme
       
        self.setStyleSheet(f"""background-color: {theme['def_bg']}; border-radius: 5px;
        color: {theme['text_color']};""")

   