from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
import os

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