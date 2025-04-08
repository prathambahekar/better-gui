from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from files.gui.ui_components import xLabel, xComboBox
from PyQt6.QtCore import Qt

class SettingsPage(QWidget):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.parent = parent  # Reference to MainWindow
        self.current_theme = theme
        self.setup_ui()

    def setup_ui(self):
        self.settings_layout = QVBoxLayout(self)
        self.settings_layout.setContentsMargins(20, 20, 20, 20)

        # Title Label
        self.settings_label = xLabel("Settings", self.current_theme, self)
        self.settings_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.settings_label.setStyleSheet(f"font-size: {self.current_theme['font_size_title']};")
        self.settings_layout.addWidget(self.settings_label)

        # Theme Section Container
        theme_container = QFrame(self)
        theme_container.setStyleSheet("background-color: #323232; border-radius: 5px; padding: 5px;")
        theme_layout = QVBoxLayout(theme_container)

        # Theme Selection
        theme_selection_layout = QHBoxLayout()
        theme_label = xLabel("Theme:", self.current_theme, self)
        self.theme_combo = xComboBox(self.current_theme, self)
        self.theme_combo.addItems(["Light", "Dark", "Custom"])
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        theme_selection_layout.addWidget(theme_label)
        theme_selection_layout.addWidget(self.theme_combo)
        theme_layout.addLayout(theme_selection_layout)
        
        self.settings_layout.addWidget(theme_container)

        # Adding Dummy Frames using a reusable function
        self.settings_layout.addWidget(self.create_frame("General Settings (Coming Soon)", "#323232"))
        self.settings_layout.addWidget(self.create_frame("Audio Settings (Coming Soon)", "#323232"))
        self.settings_layout.addWidget(self.create_frame("Privacy Settings (Coming Soon)", "#323232"))

        self.settings_layout.addStretch()

        # Apply the initial theme during setup
        self.apply_theme(self.current_theme)

    def create_frame(self, label_text, secondary_bg, height=100):
        """
        A reusable function to create a frame with a label inside.
        :param label_text: The text to be displayed in the label inside the frame
        :param secondary_bg: The background color for the frame
        :param height: The fixed height for the frame (default is 100)
        :return: The created frame
        """
        container = QFrame(self)
        container.setStyleSheet(f"background-color: {secondary_bg}; border-radius: 5px; padding: 10px;")
        container.setFixedHeight(height)  # Set the fixed height for the frame
        
        layout = QVBoxLayout(container)
        label = xLabel(label_text, self.current_theme, self)
        layout.addWidget(label)
        return container


    def change_theme(self, theme_name):
        # Dummy function to change themes (to be implemented properly in main app)
        print(f"Changing theme to: {theme_name}")

    def apply_theme(self, theme):
        self.current_theme = theme
        self.setStyleSheet(f"background-color: {theme['secondary_bg']}; color: {theme['text_color']}; font-family: {theme['font_family']};")
        
        for i in range(self.settings_layout.count()):
            item = self.settings_layout.itemAt(i)
            if item.widget() and hasattr(item.widget(), 'update_theme'):
                item.widget().update_theme(theme)
