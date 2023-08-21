# MyImports
from utils import isXorO_Time, isButtonEmpty
from styles import WINNER_HIGHLIGHT_COLOR

# Other imports
from random import randint

# PySide6 Imports
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QTimer, QEventLoop


class gameLogic:
    def __init__(self, score, gameBoard) -> None:
        self.scoreBoard = score
        self.board = gameBoard
        self.whichPlayer = randint(1, 2)  # Pair for X and odd for O

    def _registerPlayerMove(
        self,
        button: QPushButton,
        ButtonsArray,
        row: int,
        column: int,
    ):
        self.buttons = ButtonsArray

        if isXorO_Time(self.whichPlayer) == "x":
            if isButtonEmpty(button.text()):
                button.setText("X")
                button.setStyleSheet("color:red;")
                self.board[row][column] = "X"

                self.whichPlayer = self.whichPlayer - 1

                self.CheckVerticalWin()
                self.CheckHorizontalWin()
                self.checkDiagonalWin()
                self.checkTie()

        elif isXorO_Time(self.whichPlayer) == "o":
            if isButtonEmpty(button.text()):
                button.setText("O")
                button.setStyleSheet("color:green;")
                self.board[row][column] = "O"

                self.whichPlayer = self.whichPlayer + 1

                self.CheckVerticalWin()
                self.CheckHorizontalWin()
                self.checkDiagonalWin()
                self.checkTie()

            ##DEBUG
            print(self.whichPlayer, self.board)
            print(f"Button pressed: Row {row}, Column {column}")

    def CheckVerticalWin(self):
        for column in range(0, 3):
            if (
                self.board[0][column] == "X"
                and self.board[1][column] == "X"
                and self.board[2][column] == "X"
            ):
                print("X Ganhou by Vertical column")
                self.showWinnerCombination([0, 1, 2], column)
                self.scoreBoard.increasePlayerScoreByOne("X")
                self.clearButtons()
                self.resetBoardMatrix()

            elif (
                self.board[0][column] == "O"
                and self.board[1][column] == "O"
                and self.board[2][column] == "O"
            ):
                print("O Ganhou by Vertical column")
                self.showWinnerCombination([0, 1, 2], column)
                self.scoreBoard.increasePlayerScoreByOne("O")
                self.clearButtons()
                self.resetBoardMatrix()

    def CheckHorizontalWin(self):
        for row in range(0, 3):
            if (
                self.board[row][0] == "X"
                and self.board[row][1] == "X"
                and self.board[row][2] == "X"
            ):
                print("X Ganhou by Horizontal row")
                self.showWinnerCombination(row, [0, 1, 2])
                self.scoreBoard.increasePlayerScoreByOne("X")
                self.clearButtons()
                self.resetBoardMatrix()

            elif (
                self.board[row][0] == "O"
                and self.board[row][1] == "O"
                and self.board[row][2] == "O"
            ):
                print("O Ganhou by Horizontal row")
                self.showWinnerCombination(row, [0, 1, 2])
                self.scoreBoard.increasePlayerScoreByOne("O")
                self.clearButtons()
                self.resetBoardMatrix()

    def checkDiagonalWin(self):
        # FOR X
        """Checking the vertical line with a X vertical line
        [X][-][-]
        [-][X][-]
        [-][-][X]
        """

        if (
            self.board[0][2] == "X"
            and self.board[1][1] == "X"
            and self.board[2][0] == "X"
        ):
            print("X won by Diagonal -> (left to right)")
            self.showWinnerCombination([0, 1, 2], [2, 1, 0])
            self.scoreBoard.increasePlayerScoreByOne("X")
            self.clearButtons()
            self.resetBoardMatrix()

        """Checking the vertical line with a X vertical line
            [-][-][x]
            [-][x][-]
            [x][-][-]
            """
        if (
            self.board[2][2] == "X"
            and self.board[1][1] == "X"
            and self.board[0][0] == "X"
        ):
            print("X  won by Diagonal -> (right to left)")
            self.showWinnerCombination([2, 1, 0], [2, 1, 0])
            self.scoreBoard.increasePlayerScoreByOne("X")
            self.clearButtons()
            self.resetBoardMatrix()

        ## FOR O

        if (
            self.board[0][2] == "O"
            and self.board[1][1] == "O"
            and self.board[2][0] == "O"
        ):
            print("O  won by Diagonal -> (left to right)")
            self.showWinnerCombination([0, 1, 2], [2, 1, 0])
            self.scoreBoard.increasePlayerScoreByOne("O")
            self.clearButtons()
            self.resetBoardMatrix()

        """Checking the vertical line with a X vertical line
            [-][-][x]
            [-][x][-]
            [x][-][-]
            """
        if (
            self.board[2][2] == "O"
            and self.board[1][1] == "O"
            and self.board[0][0] == "O"
        ):
            print("O won by Diagonal -> (right to left)")
            self.showWinnerCombination([2, 1, 0], [2, 1, 0])
            self.scoreBoard.increasePlayerScoreByOne("O")
            self.clearButtons()
            self.resetBoardMatrix()

    def resetBoardMatrix(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def clearButtons(self):
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setText(" ")

    def checkTie(self):
        tieFlag = 0
        for row_buttons in self.buttons:
            for button in row_buttons:
                if button.text() == "X" or button.text() == "O":
                    tieFlag += 1

        if tieFlag == 9:
            print("\nTie Function\n")
            self.resetBoardMatrix()
            self.clearButtons()

    def showWinnerCombination(self, row, column):
        # Disable all buttons
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setEnabled(False)

        # Checking signals

        if isinstance(row, list) and isinstance(column, list):  # Diagonal win
            self.buttons[row[0]][column[0]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row[1]][column[1]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row[2]][column[2]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )

        elif isinstance(row, int):  # Horizontal win
            self.buttons[row][column[0]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row][column[1]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row][column[2]].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )

        elif isinstance(column, int):  # Vertical win
            self.buttons[row[0]][column].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row[1]][column].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )
            self.buttons[row[2]][column].setStyleSheet(
                f"color: {WINNER_HIGHLIGHT_COLOR};"
            )

        loop = QEventLoop()

        def resetWinnerButtons():
            # Enable all buttons
            for row_buttons in self.buttons:
                for button in row_buttons:
                    button.setEnabled(True)

            loop.quit()  # Stop the timer when the reset is done

        timer = QTimer()

        timer.timeout.connect(resetWinnerButtons)
        timer.start(1000)
        loop.exec_()
