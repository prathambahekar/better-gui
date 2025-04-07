import os
import json
import base64
import hashlib
import uuid
import shutil
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
                             QLineEdit, QListWidget, QVBoxLayout, QWidget, QPushButton, 
                             QComboBox, QDialog, QDialogButtonBox, QLabel, QHBoxLayout,QListWidgetItem)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
from win32mica import ApplyMica, MicaTheme, MicaStyle