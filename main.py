from files.ui_functions import *
from files.ui_main import Ui_MainWindow
import json
from core import *

f = open("settings.json")
Data = json.load(f) 

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		global defaultTheme

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Applying Settings
		UIFunctions.Setup_GUI(self)
		self.show()

		UIFunctions.SetTheme(self)

				
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
