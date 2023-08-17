from PySide6.QtWidgets import QPushButton, QGridLayout, QFrame
from PySide6.QtCore import Qt, Slot
from styles import MEDIUM_FONT_SIZE


class BoardFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configButtonStyle()

        # Makes the button never get focus
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def configButtonStyle(self):
        self.setStyleSheet("background:grey;height:100;width:10;")
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonGridBoard(QGridLayout):
    def __init__(self, board: QFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gameBoardLayout = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.frame = board
        self.frame.setStyleSheet(
            "background-color: lightgray; border: 1px solid black;"
        )
        self.frame.setLayout(self)

        self._createBoard

    def _createBoard(self):
        for row, text in enumerate(self._gameBoardLayout):
            for column, buttonText in enumerate(text):
                button = Button(buttonText)

                self.addWidget(button, row, column)

                buttonSlot = self._makeButtonSlot(self._registerPlayerMove)
                button.clicked.connect(buttonSlot)

    def _makeButtonSlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            method(*args, **kwargs)

        return realSlot

    def _registerPlayerMove(self):
        raise NotImplementedError
