# Imports from PySide
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout

# My imports
from styles import MEDIUM_FONT_SIZE, X_AND_O_SIZE, BIG_FONT_SIZE


class scoreBoard(QLabel):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.scorePlayerOne = 0
        self.scorePlayerTwo = 0

        self.setText(f"{self.scorePlayerOne} : {self.scorePlayerTwo}")

    def increasePlayerScoreByOne(self, player: str):
        if player == "X":
            self.scorePlayerOne += 1
        elif player == "O":
            self.scorePlayerTwo += 1

        self.updateScore()

    def updateScore(self):
        self.setText(f"{self.scorePlayerOne} : {self.scorePlayerTwo}")
        self.update()


class playerSimbol(QHBoxLayout):
    def __init__(self, score, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scoreBoard = score

        self.xSimbol = QLabel("X")
        self.oSimbol = QLabel("O")

        self.configSimbols()
        self._insertOnSimbolsOnWindow

    def configSimbols(self):
        self.scoreBoard.setStyleSheet(f"font-size:{BIG_FONT_SIZE}px; font-weight:bold;")
        # Setting up the padding
        self.scoreBoard.setContentsMargins(0, 0, 0, 0)  # (left, top, right, bottom)
        self.scoreBoard.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.xSimbol.setStyleSheet(
            f"font-size:{X_AND_O_SIZE}px; font-weight:bold;color:red"
        )
        self.xSimbol.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.xSimbol.setContentsMargins(63, 0, 0, 0)  # (left, top, right, bottom)

        self.oSimbol.setStyleSheet(
            f"font-size:{X_AND_O_SIZE}px; font-weight:bold;color:green"
        )
        self.oSimbol.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.oSimbol.setContentsMargins(0, 0, 63, 0)  # (left, top, right, bottom)

    def _insertOnSimbolsOnWindow(self):
        self.addWidget(self.xSimbol)
        self.addWidget(self.scoreBoard)
        self.addWidget(self.oSimbol)


class playerLabels(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.playerOne = QLabel("Player 1")
        self.playerTwo = QLabel("Player 2")

        self.configPlayersStyle()

        self._insertLabelOnScreen

    def configPlayersStyle(self):
        self.playerOne.setStyleSheet(
            f"font-size:{MEDIUM_FONT_SIZE}px; font-weight:bold;"
        )

        # Setting up the padding
        self.playerOne.setContentsMargins(45, 0, 0, 15)  # (left, top, right, bottom)
        self.playerOne.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.playerTwo.setStyleSheet(
            f"font-size:{MEDIUM_FONT_SIZE}px; font-weight:bold;"
        )

        # Setting up the padding
        self.playerTwo.setContentsMargins(0, 0, 45, 0)  # (left, top, right, bottom)
        self.playerTwo.setAlignment(Qt.AlignmentFlag.AlignRight)

    def _insertLabelOnScreen(self):
        self.addWidget(self.playerOne)
        self.addWidget(self.playerTwo)
