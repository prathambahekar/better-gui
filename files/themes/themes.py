from main import *
import json

f = open("settings.json")
Data = json.load(f) 

theme_load = open(f"files/themes/copilot-light.json")
Theme = json.load(theme_load) 

defaultTheme = Data["app-info"]["theme"]
default_font = Theme["default-font"]
color_1 = Theme["colors"]["color-1"]
color_2 = Theme["colors"]["color-2"]
main_border = Theme["colors"]["main-border"]
main_bg_color = Theme["colors"]["main-bg-color"]
default_font_color = Theme["default-font-color"]

def SetTheme(self): 
    self.ui.centralwidget.setStyleSheet(f"""
/* Global Styles */

* {
    
    color: {default_font_color};
    font: 600 20pt "{default_font}";
    background-color: {main_bg_color};
}

/* Left Menu QPushButton Styles */
#leftMenu .QPushButton {
    background-color: transparent;
    border-radius: {main_border};
    padding: {main_border};
    image-position: left center;
    font: 600 14pt "{default_font}";
    color: #ffffff;
}

#leftMenu .QPushButton:hover {
    background-color: #ededed;
}

#leftMenu .QPushButton:pressed {
    background-color: transparent;
}

/* Main Frame Styles */
#mainFrame {
    border: 2px solid {color_1};
    border-radius: {main_border};
}

#mainFrame .QFrame,
#mainFrame .QLabel {
    background-color: {color_1};
}

/* Icon Buttons */
#settings_btn {
    image: url(:/light/light/settings_48_regular.svg);
}

#home_btn {
    image: url(:/light/light/home_48_regular.svg);
}

#theme_btn {
    image: url(:/light/light/weather_sunny_48_regular.svg);
}

#menu_btn {
    image: url(:/light/light/panel_left_text_48_regular.svg);
}

/* Label Styles */
#stg_lbl_main {
    padding-left: 4px;
    font: 700 24pt "{default_font}";
}

/* Stacked Settings Styles */
#stack_stg .QWidget {
    border-radius: {main_border};
    background-color: {color_2};
}

/* Home App Button Labels */
#stg_home_app_bt_lbl, 
#stg_home_info_bt_lbl {
    font: 600 13pt "{default_font}";
    padding-left: 16px;
}

#stg_home_app_img_lbl, 
#stg_home_info_img_lbl {
    padding: 1{main_border};
}

#stg_home_app_hd_lbl, 
#stg_home_info_hd_lbl {
    font: 900 16pt "{default_font}";
    padding-left: 2px;
}

/* Home App Image Buttons */
#stg_home_app_img_btn, 
#stg_home_info_img_btn {
    font: 600 14pt "{default_font}";
    padding-left: 4px;
    border: 0px;
}

/* Page Background Styles */
#home_page, 
#setting_page, 
#info_page, 
#stg_abt_pg, 
#stg_home_pg, 
#stg_app_pg {
    background-color: {color_1};
}
""")
