# MyImports
from utils import isXorO_Time, isButtonEmpty

# Other imports
from random import randint

# PySide6 Imports
from PySide6.QtWidgets import QPushButton


class gameLogic:
    def __init__(self, score, gameBoard) -> None:
        self.scoreBoard = score
        self.board = gameBoard
        self.whichPlayer = randint(1, 2)  # Pair for X and odd for O

    def _registerPlayerMove(
        self, button: QPushButton, ButtonClearMethod, checkTie, row: int, column: int
    ):
        if isXorO_Time(self.whichPlayer) == "x":
            if isButtonEmpty(button.text()):
                button.setText("X")
                button.setStyleSheet("color:red;")
                self.board[row][column] = "X"

                self.whichPlayer = self.whichPlayer - 1

                self.CheckVerticalWin(ButtonClearMethod)
                self.CheckHorizontalWin(ButtonClearMethod)
                self.checkDiagonalWin(ButtonClearMethod)
                checkTie()

        elif isXorO_Time(self.whichPlayer) == "o":
            if isButtonEmpty(button.text()):
                button.setText("O")
                button.setStyleSheet("color:green;")
                self.board[row][column] = "O"

                self.whichPlayer = self.whichPlayer + 1

                self.CheckVerticalWin(ButtonClearMethod)
                self.CheckHorizontalWin(ButtonClearMethod)
                self.checkDiagonalWin(ButtonClearMethod)
                checkTie()

            ##DEBUG
            print(self.whichPlayer, self.board)
            print(f"Button pressed: Row {row}, Column {column}")

    def CheckVerticalWin(self, ButtonClearMethod):
        for column in range(0, 3):
            if (
                self.board[0][column] == "X"
                and self.board[1][column] == "X"
                and self.board[2][column] == "X"
            ):
                print("X Ganhou")
                self.scoreBoard.increasePlayerScoreByOne("X")
                ButtonClearMethod()
                self.resetBoardMatrix()

            elif (
                self.board[0][column] == "O"
                and self.board[1][column] == "O"
                and self.board[2][column] == "O"
            ):
                print("O Ganhou")
                self.scoreBoard.increasePlayerScoreByOne("O")
                ButtonClearMethod()
                self.resetBoardMatrix()

    def CheckHorizontalWin(self, ButtonClearMethod):
        for row in range(0, 3):
            if (
                self.board[row][0] == "X"
                and self.board[row][1] == "X"
                and self.board[row][2] == "X"
            ):
                print("X Ganhou")
                self.scoreBoard.increasePlayerScoreByOne("X")
                ButtonClearMethod()
                self.resetBoardMatrix()

            elif (
                self.board[row][0] == "O"
                and self.board[row][1] == "O"
                and self.board[row][2] == "O"
            ):
                print("O Ganhou")
                self.scoreBoard.increasePlayerScoreByOne("O")
                ButtonClearMethod()
                self.resetBoardMatrix()

    def checkDiagonalWin(self, ButtonClearMethod):
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
            print("X Ganhou")
            self.scoreBoard.increasePlayerScoreByOne("X")
            ButtonClearMethod()
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
            print("X Ganhou")
            self.scoreBoard.increasePlayerScoreByOne("X")
            ButtonClearMethod()
            self.resetBoardMatrix()

        ## FOR O

        if (
            self.board[0][2] == "O"
            and self.board[1][1] == "O"
            and self.board[2][0] == "O"
        ):
            print("O Ganhou")
            self.scoreBoard.increasePlayerScoreByOne("O")
            ButtonClearMethod()
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
            print("O Ganhou")
            self.scoreBoard.increasePlayerScoreByOne("O")
            ButtonClearMethod()
            self.resetBoardMatrix()

    def resetBoardMatrix(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
