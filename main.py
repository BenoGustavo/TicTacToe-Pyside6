# Other imports
import sys

# PySide Imports
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# My Imports
from styles import setupTheme
from player_names import playerLabels, playerSimbol
from main_window import MainWindow
from tittle import tittleLabel
from board import ButtonGridBoard, BoardFrame

if __name__ == "__main__":
    # Creating the app
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Adding the tittle to the Layout
    tittleWidget = tittleLabel("Tic-Tac-Toe")
    window.addWidgetToVLayout(tittleWidget)

    playerSimbols = playerSimbol()
    window.vLayout.addLayout(playerSimbols)

    playerSimbols._insertOnSimbolsOnWindow()

    playerLabel = playerLabels()
    window.vLayout.addLayout(playerLabel)

    playerLabel._insertLabelOnScreen()

    BoardInstance = BoardFrame()

    board = ButtonGridBoard(board=BoardInstance)
    # window.vLayout.addLayout(board)

    window.vLayout.addWidget(BoardInstance, alignment=Qt.AlignmentFlag.AlignCenter)

    board._createBoard()

    # Remove the permission to resize the window
    window.AdjustFixedSize()

    # Execute the app
    window.show()
    app.exec()
