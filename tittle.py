#Imports from PySide
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

#My Imports
from styles import BIG_FONT_SIZE

class tittleLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.configTittleStyle()

    def configTittleStyle(self):
        self.setStyleSheet(f"font-size:{BIG_FONT_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter,Qt.AlignmentFlag.AlignTop)