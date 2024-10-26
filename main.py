from files.ui_functions import *
from files.ui_main import Ui_MainWindow
import json
from core import *
from files.themes.themes import SetTheme

acess_settings = open("settings.json")
Data = json.load(acess_settings) 

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		global defaultTheme

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Applying Settings
		UIFunctions.Setup_GUI(self)
		UIFunctions.ToggleMenu(self, 50, 300)


		self.show()
		UIFunctions.SetTheme(self)
		# SetTheme(self)
		

	
	
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	window = MainWindow()
	
	sys.exit(app.exec())
