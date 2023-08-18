# MyImports
from utils import isXorO_Time, isButtonEmpty

# Other imports
from random import randint

# PySide6 Imports
from PySide6.QtWidgets import QPushButton


class gameLogic:
    def __init__(self) -> None:
        self.whichPlayer = randint(1, 2)  # Pair for X and odd for O

    def _registerPlayerMove(self, button: QPushButton, row: int, column: int):
        if isXorO_Time(self.whichPlayer) == "x":
            if isButtonEmpty(button.text()):
                button.setText("X")
                button.setStyleSheet("color:red;")

                self.whichPlayer = self.whichPlayer - 1

        elif isXorO_Time(self.whichPlayer) == "o":
            if isButtonEmpty(button.text()):
                button.setText("O")
                button.setStyleSheet("color:green;")

                self.whichPlayer = self.whichPlayer + 1

        print(self.whichPlayer)
        print(f"Button pressed: Row {row}, Column {column}")
