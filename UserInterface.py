from InterfaceProperties import Properties

from copy import copy
from numpy import array, dstack, uint8

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *





class MainApplication(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.stylesheet = Properties.light_mode
        self.setStyleSheet(self.stylesheet)
    
    
    
    def __initializeCommonVariables(self):
        ...