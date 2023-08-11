# Other imports
import sys

# PySide Imports
from PySide6.QtWidgets import QApplication

# My Imports
from styles import setupTheme
from player_names import playerLabels, playerSimbol
from main_window import MainWindow
from tittle import tittleLabel

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

    # Remove the permission to resize the window
    window.AdjustFixedSize()

    # Execute the app
    window.show()
    app.exec()
