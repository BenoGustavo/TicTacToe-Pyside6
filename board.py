# PySide6 Imports
from PySide6.QtWidgets import QPushButton, QGridLayout, QFrame
from PySide6.QtCore import Qt, Slot

# My Imports
from styles import MEDIUM_FONT_SIZE


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
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonGridBoard(QGridLayout):
    def __init__(self, board: QFrame, gameLogicClass, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameLogicInstance = gameLogicClass()

        self._gameBoardLayout = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.frame = board
        self.frame.setLayout(self)

        self._createBoard

    def _createBoard(self):
        for row, text in enumerate(self._gameBoardLayout):
            for column, buttonText in enumerate(text):
                button = Button(buttonText)

                button.setProperty("cssClass", "ButtonCSS")
                self.addWidget(button, row, column)

                buttonSlot = self._makeButtonSlot(
                    method=self.gameLogicInstance._registerPlayerMove,
                    row=row,
                    column=column,
                )

                button.clicked.connect(buttonSlot)

    def _makeButtonSlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            method(*args, **kwargs)

        return realSlot
