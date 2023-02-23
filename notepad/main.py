from sys import argv, exit
from uic.notepad import UiNotepad
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QFontDatabase


class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()

        self.main_ui = UiNotepad()
        self.main_ui.setup_ui(self)

        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')


if __name__ == "__main__":
    application = QApplication(argv)
    main_window = Notepad()
    main_window.show()
    exit(application.exec())
