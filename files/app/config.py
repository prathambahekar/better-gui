import os


SETTINGS = {
    "app" : {
        "name" : "App",
        "version" : "v0.0.1",
        "build" : "dev"
    },
    "theme" : "default",
    "menu_bar_enabled" : False,
    "is_mica" : True
    
}

# thene

# accent colors
# rgb(196, 220, 255) or #9ecbff

# Unified Style Configurations for both dark and light themes
STYLE_CONFIG_DARK = {
    "font_family": "Inter, Segoe UI, Roboto, Arial, sans-serif",
    "font_size_large": "12pt",
    "font_size_medium": "10pt",
    "font_size_title": "16pt",
    "text_color": "#e0e0e0",
    "bg_color": "transparent",
    "secondary_bg": "#252525",
    "def_bg": "#2c2c2c",
    "border_color": "#3a3a3a",
    "accent_color": "#9ecbff",
    "accent_hover": "#c4d8ff",
    "accent_pressed": "#9ecbff",
    "hover_bg": "#2d2d2d",
    "selected_bg": "#b9a6d3",
    "selected_text_color": "#1e1e1e",
    # Sidebar/button specific
    "button_bg": "#2c2c2c",
    "button_hover": "#3c3c3c",
    "button_pressed": "#252525",
    "button_active_bg": "#252525",
    "separator_color": "#555555",
    "icon_color": "#f7f7f7",
    "link_color": "#1e90ff",
}

STYLE_CONFIG_LIGHT = {
    "font_family": "Inter, Segoe UI, Roboto, Arial, sans-serif",
    "font_size_large": "12pt",
    "font_size_medium": "10pt",
    "font_size_title": "16pt",
    "text_color": "#333333",
    "bg_color": "transparent",
    "secondary_bg": "#f5f6fa",
    "def_bg": "#ffffff",
    "border_color": "#d0d0d0",
    "accent_color": "#185abd",
    "accent_hover": "#185abd",
    "accent_pressed": "#185abd",
    "hover_bg": "#e8e8e8",
    "selected_bg": "#185abd",
    "selected_text_color": "white",
    # Sidebar/button specific
    "button_bg": "#fcfcfc",
    "button_hover": "#e8e8e8",
    "button_pressed": "#e0e0e0",
    "button_active_bg": "#e0e0e0",
    "separator_color": "#cccccc",
    "icon_color": "#1a1a1a",
    "link_color": "#185abd",
}