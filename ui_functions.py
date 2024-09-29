from main import *
import json

f = open("settings.json")
Data = json.load(f) 

defaultTheme = Data["app-info"]["theme"]


class UIFunctions(MainWindow):

	def SetTheme(self):
		
		str = open(f"Themes\{defaultTheme}.qss", 'r').read()
		self.ui.centralwidget.setStyleSheet(str)

	def SwitchTheme(self):

		global defaultTheme

		if defaultTheme == "Light":
			str = open(f"Themes\Dark.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "Dark"

		elif defaultTheme == "Dark":
			str = open(f"Themes\Light.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "Light"

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
			self.ui.info_btn.setText("About")

		elif presentWidth == max:
			startToggle = max
			endToggle = min

			self.ui.home_btn.setText("")
			self.ui.settings_btn.setText("")
			self.ui.theme_btn.setText("")
			self.ui.info_btn.setText("")


		self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
		self.animation.setDuration(200)
		self.animation.setStartValue(startToggle)
		self.animation.setEndValue(endToggle)
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def AboutApp(self):

		About_txt = Data["app-info"]["name"]
		Version_txt = Data["app-info"]["version"]
		Creator_txt = Data["app-info"]["developer"]
		Build_txt = Data["app-info"]["build"]

		self.ui.about_lbl.setText(f"About {About_txt}")
		self.ui.version_lbl.setText(f"Version - {Version_txt}")
		self.ui.creator_lbl.setText(f"Developer - {Creator_txt}")
		self.ui.build_lbl.setText(f"Build - {Build_txt}")


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
		self.ui.info_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(2))

		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))
