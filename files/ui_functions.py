from main import *
import json
import os
import darkdetect

load_settings = open("settings.json")
Data = json.load(load_settings) 
defaultTheme = Data["app-info"]["theme"]


class UIFunctions(MainWindow):

	def SetTheme(self):
		
		if defaultTheme == "sys":
			checkTheme = darkdetect.isDark()
			# print(checkTheme)
			if checkTheme == True:
				str = open(f"files/themes/dark.qss", 'r').read()
				self.ui.centralwidget.setStyleSheet(str)
			else:
				str = open(f"files/themes/light.qss", 'r').read()
				self.ui.centralwidget.setStyleSheet(str)

		else:
			str = open(f"files/themes/{defaultTheme}.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)
		
	def SwitchTheme(self):
		global defaultTheme

		# Directory where your .qss files are located
		qss_directory = "files/themes"

		# Get a list of all .qss files in the directory
		qss_files = [file for file in os.listdir(qss_directory) if file.endswith(".qss")]

		# Find the index of the current theme
		try:
			current_index = qss_files.index(defaultTheme + ".qss")
		except ValueError:
			current_index = -1

		# Calculate the next theme index
		next_index = (current_index + 1) % len(qss_files)
		next_theme = qss_files[next_index].replace(".qss", "")

		# Read and apply the next theme
		with open(os.path.join(qss_directory, qss_files[next_index]), 'r') as f:
			stylesheet = f.read()
		self.ui.centralwidget.setStyleSheet(stylesheet)
		defaultTheme = next_theme

		if Data["app-info"]["mica"]["enable"] == True:
			if defaultTheme == "light":
				ApplyMica(self.winId(), MicaTheme.LIGHT, MicaStyle.DEFAULT)
			elif defaultTheme == "dark":
				ApplyMica(self.winId(), MicaTheme.DARK, MicaStyle.DEFAULT)

	def ToggleMenu(self, min, max):

		presentWidth = self.ui.leftMenu.width()

		startToggle = ""
		endToggle = ""

		if presentWidth == min:
			startToggle = min
			endToggle = max
			
			self.ui.home_btn.setText("Home")
			self.ui.settings_btn.setText("Settings")
			self.ui.theme_btn.setText("Theme")

		elif presentWidth == max:
			startToggle = max
			endToggle = min

			self.ui.home_btn.setText("")
			self.ui.settings_btn.setText("")
			self.ui.theme_btn.setText("")


		self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
		self.animation.setDuration(200)
		self.animation.setStartValue(startToggle)
		self.animation.setEndValue(endToggle)
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def AboutApp(self):

		pass


	def Setup_GUI(self):

		# set window title
		self.setWindowTitle(Data["app-info"]["name"])

		UIFunctions.AboutApp(self)

		# set windows default size
		self.resize(Data["app-info"]["window-size"]["default"][0], Data["app-info"]["window-size"]["default"][1])

		# set window min size
		if Data["app-info"]["window-size"]["isMin"] != False:
			self.setMinimumSize(Data["app-info"]["window-size"]["min"][0], Data["app-info"]["window-size"]["min"][1])
		
		# set window max size
		if Data["app-info"]["window-size"]["isMax"] != False:
			self.setMaximumSize(Data["app-info"]["window-size"]["max"][0], Data["app-info"]["window-size"]["max"][1])
			

		self.ui.home_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(0))
		self.ui.settings_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(1))

		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))

		WindowIcon = QIcon()
		WindowIcon.addFile("icon.ico")
		self.setWindowIcon(WindowIcon)

		
		if Data["app-info"]["mica"]["enable"] == True:
			self.setAttribute(Qt.WA_TranslucentBackground)
			ApplyMica(self.winId(), MicaTheme.AUTO, MicaStyle.DEFAULT)