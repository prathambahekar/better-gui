import json

# importing core modules
from core import *

# importing ui files
from files.ui.ui_functions import *
from files.ui.ui_main import Ui_MainWindow

# importing app files
# from files.app_functions import AppFunctions

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		global defaultTheme

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Applying UI Settings
		UIFunctions.Setup_GUI(self)

		# Applying App Settings
		# AppFunctions.Setup_App(self)

		self.show()
		
		#setting theme
		UIFunctions.SetTheme(self)
		
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
