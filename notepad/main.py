from sys import argv, exit
from interface.notepad_ui import UiNotepad
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt
from interface.config import NotepadConfig


class Notepad(QMainWindow, NotepadConfig):
    def __init__(self):
        super(Notepad, self).__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.main_ui = UiNotepad()
        self.main_ui.setup_ui(self)

        self.main_ui.close.clicked.connect(self.close)
        self.main_ui.delete_note.clicked.connect(self.clear)
        self.main_ui.save.clicked.connect(self.savenote)

        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')

    def savenote(self) -> None:
        title, note = self.main_ui.title.text(), self.main_ui.note.toPlainText()
        if not title or not note:
            QMessageBox.warning(self, 'Notepad', 'Не все поля заполнены. Заполните все формы для сохранения!')
        else:
            data: list = self.readnotes()
            try:
                values = self.get_values()
                if title.lower() in values or note.lower in values:
                    QMessageBox.warning(self, 'Notepad', 'Заметка с таким заголовком или текстом уже существует!')
                else:
                    self.append_data(data, title, note)
            except IndexError:
                self.append_data(data, title, note)
            finally:
                self.dump_note(data)
                # emmit commit signals

    def clear(self) -> None:
        self.main_ui.title.setText('')
        self.main_ui.note.setPlainText('')


def run():
    application, main_window = QApplication(argv), Notepad()
    main_window.show()
    exit(application.exec())
