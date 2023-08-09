#Other imports
import sys

#PySide Imports
from PySide6.QtWidgets import QApplication

#My Imports
from main_window import MainWindow
from tittle import tittleLabel

if __name__ == "__main__":

    #Creating the app
    app = QApplication(sys.argv)
    window = MainWindow(app=app)

    #Adding the tittle to the Layout
    tittleWidget = tittleLabel()
    window.addWidgetToVLayout(tittleWidget)

    window.show()
    app.exec()
