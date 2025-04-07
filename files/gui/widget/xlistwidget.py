# custom_listwidget.py
from PyQt6.QtWidgets import QListWidget, QWidget, QVBoxLayout

class xListWidget(QWidget):
    def __init__(self, theme, parent=None):
        super().__init__(parent)
        self.current_theme = theme
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)
        self.apply_theme()

    def apply_theme(self):
        theme = self.current_theme
        # Note: Scrollbar styling will be handled by CustomScrollBar, so we focus on list-specific styles here
        self.list_widget.setStyleSheet(f"""
            QListWidget {{
                background-color: {theme['secondary_bg']};
                border: 1px solid {theme['border_color']};
                border-radius: 10px;
                padding: 10px;
                font: {theme['font_size_large']} "{theme['font_family']}";
                color: {theme['text_color']};
                outline: none;
            }}
            QListWidget::item {{
                padding: 8px;
                border-radius: 8px;
            }}
            QListWidget::item:selected {{
                background-color: {theme['accent_color']};
                color: {theme['selected_text_color']};
                border-radius: 6px;
            }}
            
        """)

    def update_theme(self, new_theme):
        self.current_theme = new_theme
        self.apply_theme()

    def add_item(self, item_text):
        self.list_widget.addItem(item_text)

    def clear(self):
        self.list_widget.clear()

    def current_item(self):
        return self.list_widget.currentItem()

    def count(self):
        return self.list_widget.count()

    def item(self, index):
        return self.list_widget.item(index)

    def set_current_row(self, row):
        self.list_widget.setCurrentRow(row)