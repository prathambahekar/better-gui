from main import *
from winreg import *



class UIDark(MainWindow):
   
	def GetAccentColor(self):
		# Connect to the registry and retrieve the accent color
		registry = ConnectRegistry(None, HKEY_CURRENT_USER)
		key = OpenKey(registry, r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Explorer\\Accent')
		key_value = QueryValueEx(key, 'AccentColorMenu')
		accent_int = key_value[0]
		accent = accent_int - 4278190080
		accent = str(hex(accent)).split('x')[1]
		accent = accent[4:6] + accent[2:4] + accent[0:2]  # Reorder to RGB
		return 'rgb' + str(tuple(int(accent[i:i + 2], 16) for i in (0, 2, 4)))

	def SetStyleSheetDark(self):
		# Define color variables
		background_color = "transparent"
		primary_color = "#1e1e1e"
		secondary_color = "#2c2c2c"
		border_color = "#202326"
		hover_color = "#3a3a3a"
		pressed_color = "#2b2b2b"
		text_color = "#e0e0e0"
		button_text_color = "#ffffff"
		header_font = "700 18pt 'Consolas'"
		button_font = "600 14pt 'Consolas'"
		accent_color = UIDark.GetAccentColor(self)

		# Use the accent color in the stylesheet
		self.ui.centralwidget.setStyleSheet(f"""
			/* General Styles */
			* {{
				background-color: {background_color};
				font: 600 18pt "Consolas";
				color: {text_color};
			}}

			/* TABWIDGET */
			.QTabWidget {{
			}}

			.QWidget {{
				border-radius: 5px;
			}}

			.QTabWidget::pane {{
				border: 1px solid rgb(43, 43, 43);
				border-radius: 5px;
			}}

			.QTabWidget::tab-bar {{
				left: 5px;
			}}

			.QTabBar::tab {{
				background-color: rgba(255, 255, 255, 0);
				padding: 7px 15px;
				margin-right: 2px;
			}}

			.QTabBar::tab:hover {{
				background-color: rgba(255, 255, 255, 13);
				border-top-left-radius: 5px;
				border-top-right-radius: 5px;
			}}

			.QTabBar::tab:selected {{
				background-color: rgba(255, 255, 255, 16);
				border-top-left-radius: 5px;
				border-top-right-radius: 5px;
			}}

			.QTabBar::tab:disabled {{
				color: rgb(150, 150, 150);
			}}

			/* LINEEDIT */
			.QLineEdit {{
				background-color: rgba(255, 255, 255, 16);
				border: 1px solid rgba(255, 255, 255, 13);
				font-size: 16px;
				font-family: "Segoe UI", serif;
				font-weight: 500;
				border-radius: 7px;
				border-bottom: 1px solid rgba(255, 255, 255, 150);
				padding-top: 0px;
				padding-left: 5px;
			}}

			.QLineEdit:hover {{
				background-color: rgba(255, 255, 255, 20);
				border: 1px solid rgba(255, 255, 255, 10);
				border-bottom: 1px solid rgba(255, 255, 255, 150);
			}}

			.QLineEdit:focus {{
				border-bottom: 2px solid {accent_color};
				background-color: rgba(255, 255, 255, 5);
				border-top: 1px solid rgba(255, 255, 255, 13);
				border-left: 1px solid rgba(255, 255, 255, 13);
				border-right: 1px solid rgba(255, 255, 255, 13);
			}}

			.QLineEdit:disabled {{
				color: rgb(150, 150, 150);
				background-color: rgba(255, 255, 255, 13);
				border: 1px solid rgba(255, 255, 255, 5);
			}}

			/* PUSHBUTTON */
			.QPushButton {{
				background-color: {secondary_color};
				/*border: 1px solid rgba(255, 255, 255, 13);*/
				border-radius: 7px;
				/*min-height: 38px;*/
				/*max-height: 38px;*/
			}}

			.QPushButton:hover {{
				background-color: {hover_color};
				/*border: 1px solid rgba(255, 255, 255, 10);*/
			}}

			.QPushButton::pressed {{
				background-color: {pressed_color};
				border: 1px solid rgba(255, 255, 255, 13);
				color: rgba(255, 255, 255, 200);
			}}

			.QPushButton::disabled {{
				color: rgb(150, 150, 150);
				background-color: rgba(255, 255, 255, 13);
			}}

			/* Left Menu Button Styles */
			#leftMenu .QPushButton {{
				background-color: {background_color};
				border-radius: 7px;
				padding: 7px;
				image-position: left center;
				font: {button_font};
				color: {button_text_color};
			}}

			#leftMenu .QPushButton:hover {{
				background-color: {hover_color};
			}}

			#leftMenu .QPushButton:pressed {{
				background-color: {pressed_color};
			}}

			/* Main Frame Styles */
			#mainFrame {{
				border: 2px solid {border_color};    
				border-radius: 7px;
			}}

			#mainFrame .QFrame, 
			#mainFrame .QLabel {{
				background-color: {primary_color};
			}}

			

			/* Button Icons */
			#settings_btn {{
				image: url(:/dark/dark/settings_48_regular.svg);
			}}

			#home_btn {{
				image: url(:/dark/dark/home_48_regular.svg);
			}}

			#theme_btn {{
				image: url(:/dark/dark/weather_sunny_48_regular.svg);
			}}

			#menu_btn {{
				image: url(:/dark/dark/panel_left_text_48_regular.svg);
			}}

			/* Section Header Styles */
			#stg_lbl_main {{
				padding-left: 4px;
				font: {header_font};
			}}

			/* Stack Settings */
			#stack_stg .QWidget {{
				border-radius: 8px;
				background-color: {secondary_color}; /* Updated for better contrast */
			}}

			/* Home App Button Styles */
			#stg_home_app_bt_lbl, 
			#stg_home_info_bt_lbl {{
				font: 600 13pt "Consolas";
				padding-left: 16px;
			}}

			#stg_home_app_img_lbl, 
			#stg_home_info_img_lbl {{
				padding: 17px;
			}}

			#stg_home_app_hd_lbl, 
			#stg_home_info_hd_lbl {{
				font: 900 16pt "Consolas";
				padding-left: 2px;
			}}

			#stg_home_app_img_btn, 
			#stg _home_info_img_ btn {{
				font: 600 14pt "Consolas";
				padding-left: 4px;
				border: 0px;
			}}

			/* Page Background Colors */
			#home_page, 
			#setting_page, 
			#info_page, 
			#stg_abt_pg, 
			#stg_home_pg, 
			#stg_app_pg {{
				background-color: {primary_color};
			}}

			

			/*MENU*/
.QMenuBar {{
    background-color: transparent;
    color: white;
    padding: 10px;
    font-size: 17px;
    font-weight: 400;
}}

.QMenuBar::item {{
    background-color: transparent;
    padding: 10px 13px;
    margin-left: 5px;
    border-radius: 5px;
}}

.QMenuBar::item:selected {{
    background-color: rgb(255, 255, 255, 20);
}}

.QMenuBar::item:pressed {{
    background-color: rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
}}

.QMenu {{
    background-color: {primary_color};
    padding-left: 1px;
    padding-top: 1px;
    border-radius: 5px;
    border: 1px solid rgb(255, 255, 255, 13);
}}

.QMenu::item {{
    background-color: {primary_color};
    padding: 5px 15px;
    border-radius: 5px;
    min-width: 60px;
    margin: 3px;
}}

.QMenu::item:selected {{
    background-color: {hover_color};
}}

.QMenu::item:pressed {{
    background-color: {pressed_color};
}}

.QMenu::right-arrow {{
    image: url(:/dark/dark/chevron_right_48_filled.svg);
    min-width: 40px;
    min-height: 18px;
}}

.QMenuBar:disabled {{
    color: rgb(150, 150, 150);
}}

.QMenu::item:disabled {{
    color: rgb(150, 150, 150);
    background-color: transparent;
}}















		""")