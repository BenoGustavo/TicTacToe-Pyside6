# PySide6 Imports
from PySide6.QtWidgets import QPushButton, QGridLayout, QFrame
from PySide6.QtCore import Qt, Slot

# My Imports
from styles import BIG_FONT_SIZE


class BoardFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configFrame()

    def configFrame(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(400, 400)

        # Placeholder CSS
        self.setStyleSheet("border: 2px solid white;")


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configButtonStyle()

        # Makes the button never get focus
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def configButtonStyle(self):
        self.setFixedSize(100, 100)  # w,h
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)


class ButtonGridBoard(QGridLayout):
    def __init__(self, board: QFrame, gameLogicClass, score, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gameBoardLayout = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.buttons = []  # Store button instances in a 2D list

        self.scoreBoard = score

        self.gameLogicInstance = gameLogicClass(self.scoreBoard, self._gameBoardLayout)

        self.frame = board
        self.frame.setLayout(self)

        self._createBoard

    def _createBoard(self):
        for row, text in enumerate(self._gameBoardLayout):
            row_buttons = []
            for column, buttonText in enumerate(text):
                button = Button(buttonText)

                button.setProperty("cssClass", "ButtonCSS")
                self.addWidget(button, row, column)

                buttonSlot = self._makeButtonSlot(
                    self.gameLogicInstance._registerPlayerMove,
                    button,
                    self.clearButtons,
                    self.checkTie,
                    row=row,
                    column=column,
                )

                button.clicked.connect(buttonSlot)

                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def _makeButtonSlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            method(*args, **kwargs)

        return realSlot

    def clearButtons(self):
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setText(" ")

    # IT NEEDED TO BE PART OF THE GAMES LOGIC BUT I WILL LEAVE IT HERE
    # BECAUSE IT WILL DO LESS WORK
    def checkTie(self):
        tieFlag = 0
        for row_buttons in self.buttons:
            for button in row_buttons:
                if button.text() == "X" or button.text() == "O":
                    tieFlag += 1

        if tieFlag == 9:
            print("reset")
            self.clearButtons()
