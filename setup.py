import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','Themes', 'settings.json', "ui_functions.py"]

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "User Interface",
    version = "1.0.0",
    description = "A Modern GUI",
    author = "Pratham H Bahekar",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
