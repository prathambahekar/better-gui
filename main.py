import sys
import os, json
from ui_functions import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow

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
