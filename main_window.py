# My Imports

# Imports from QT
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Window Tittle
        self.setWindowTitle("Tic-Tac-Toe")

        # Basic Layout
        self.centralWidget = QWidget()
        self.vLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.vLayout)
        self.setCentralWidget(self.centralWidget)

        # Setting up icons
        # self.setWindowIcon(Later:put icon path here)
        # app.setWindowIcon(Later:put icon path here)

    def AdjustFixedSize(self):
        # NEEDS TO BE THE LAST THING SETTED
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
