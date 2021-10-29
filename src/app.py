from PyQt5.QtWidgets import *
from gui import MainWindow


class App:

    def __init__(self):
        self.app = QApplication([])
        self.win = MainWindow()
        self.win.show()
        self.app.exec_()


# run task scheduler with GUI
if __name__ == '__main__':
    App()
