from sys import argv, exit
from uic.notepad import UiNotepad
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt


class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.main_ui = UiNotepad()
        self.main_ui.setup_ui(self)

        self.main_ui.close.clicked.connect(lambda: self.close())

        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')


def run():
    application = QApplication(argv)
    main_window = Notepad()
    main_window.show()
    exit(application.exec())
