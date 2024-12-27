from files.ui.ui_functions import *
# from files.app_functions import AppFunctions
from files.ui.ui_main import Ui_MainWindow
import json
from core import *
<<<<<<< HEAD
from files.ui.blurwindow import *
=======
from files.themes.themes import SetTheme

access_settings = open("settings.json")
Data = json.load(access_settings) 
>>>>>>> 414d6d3686c665065cf67e7136d0013e986c82b8

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
		UIFunctions.SetTheme(self)
		
		
		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
