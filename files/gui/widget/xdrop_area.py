from files.gui.modules import *
import files.app.config as config


theme_dark = config.STYLE_CONFIG_DARK
theme_light = config.STYLE_CONFIG_LIGHT


class DropArea(QLabel):
    def __init__(self, parent=None, theme=theme_dark):
        super().__init__("Drag and Drop Files or Folders Here\nor Click to Select", parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.apply_theme(theme)
        self.setAcceptDrops(True)
        self.parent = parent

    def apply_theme(self, theme):
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {theme['secondary_bg']};
                border: 2px dashed {theme['accent_color']};
                border-radius: 10px;
                font: {theme['font_size_large']} "{theme['font_family']}";
                color: {theme['text_color'] if theme == theme_light else '#aaaaaa'};
                padding: 20px;
            }}
            QLabel:hover {{
                background-color: {theme['hover_bg']};
                border-color: {theme['accent_color']};
            }}
        """)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            item_path = urls[0].toLocalFile()
            if os.path.exists(item_path):
                self.parent.item_path = item_path
                self.setText(f"Selected: {os.path.basename(item_path)}")
                self.parent.lock_item()