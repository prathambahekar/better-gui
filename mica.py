import sys
import ctypes
from win32mica import ApplyMica, MicaTheme, MicaStyle
from PySide6 import QtWidgets, QtCore

class MicaWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window to be translucent and initialize Mica
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Qt Dark")
        self.setGeometry(100, 100, 300, 200)

        # Apply Mica effect
        ApplyMica(self.winId(), MicaTheme.DARK, MicaStyle.DEFAULT)

        # Create labels
        self.label1 = QtWidgets.QLabel("Change the system theme\nfrom the settings!", self)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setGeometry(10, 10, 280, 80)  # Set geometry for label
        self.label1.setStyleSheet("color: black;")  # Set initial text color

        self.label2 = QtWidgets.QLabel("Another label with the same text.", self)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setGeometry(10, 100, 280, 80)  # Set geometry for label
        self.label2.setStyleSheet("color: black;")  # Set initial text color

        # Apply styles based on theme
        self.apply_style_sheet(MicaTheme.DARK)

    def apply_style_sheet(self, theme):
        """Apply styles based on the current theme."""
        if theme == MicaTheme.DARK:
            self.label1.setStyleSheet("background-color: rgba(255, 255, 255, 200); color: black;")
            self.label2.setStyleSheet("background-color: rgba(255, 255, 255, 200); color: black;")
        else:
            self.label1.setStyleSheet("background-color: rgba(0, 0, 0, 200); color: white;")
            self.label2.setStyleSheet("background-color: rgba(0, 0, 0, 200); color: white;")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MicaWindow()
    window.show()
    sys.exit(app.exec())
