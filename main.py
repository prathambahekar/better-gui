from files.gui.modules import *
from files.gui.ui_main import MainWindow




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())