from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Qt
from styles import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configButtonStyle()

        # Makes the button never get focus
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def configButtonStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonGridBoard(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gameBoardLayout = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self._createBoard

    def _createBoard(self):
        for row, text in enumerate(self._gameBoardLayout):
            for column, buttonText in enumerate(text):
                button = Button(buttonText)
