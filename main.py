from sys import argv, exit
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QListWidgetItem
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt
from webbrowser import open_new_tab

from notepad_ui import UiNotepad
from config import NotepadConfig
from note_ui import UiNote


class NoteWindow(QMainWindow, NotepadConfig):
    def __init__(self):
        super(NoteWindow, self).__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')

        self.note_ui = UiNote()
        self.note_ui.setup_ui(self)

    def open_note(self, id_note: int):
        try:
            data = self.readnotes()[id_note]
            self.note_ui.title.setText(f"{data['title']}")
            self.note_ui.note.setPlainText(data['note'])
            self.show()
        except IndexError:
            pass


class Notepad(QMainWindow, NotepadConfig):
    def __init__(self):
        super(Notepad, self).__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        QFontDatabase.addApplicationFont('fonts/Rubik-Regular.ttf')

        self.main_ui = UiNotepad()
        self.main_ui.setup_ui(self)

        self.note_window = NoteWindow()

        self.main_ui.close.clicked.connect(self.close)
        self.main_ui.delete_note.clicked.connect(self.clear)
        self.main_ui.save.clicked.connect(self.savenote)
        self.main_ui.logo.clicked.connect(lambda: open_new_tab('https://github.com/Fantaz1er/notepad'))
        self.main_ui.notes.clicked.connect(lambda: self.note_window.open_note(self.main_ui.notes.currentRow()))
        self.note_window.note_ui.close.clicked.connect(self.note_window.close)
        self.note_window.note_ui.delete_note.clicked.connect(lambda: self.delete_note(self.main_ui.notes.currentRow()))
        self.note_window.note_ui.save.clicked.connect(lambda: self.edit(self.main_ui.notes.currentRow()))

    def savenote(self) -> None:
        title, note = self.main_ui.title.text().strip(), self.main_ui.note.toPlainText().strip()
        if not title or not note:
            QMessageBox.warning(self, 'Notepad', 'Не все поля заполнены. Заполните все формы для сохранения!')
        else:
            data: list = self.readnotes()
            values = self.get_values()
            if title.lower() in values or note.lower() in values:
                QMessageBox.warning(self, 'Notepad', 'Заметка с таким заголовком или текстом уже существует!')
            else:
                if self.get_count_notes == 0:
                    self.main_ui.notes.clear()
                self.append_data(data, title, note)
                self.dump_note(data)
                self.add_item()
                self.clear()

    def add_item(self) -> None:
        item = QListWidgetItem()
        item.setFont(self.main_ui.font_notes)
        self.main_ui.notes.addItem(item)
        data = self.readnotes()[-1]
        item.setText(f"{data['title'].capitalize()}\n\n\n{data['date']}\t{' '.join(data['note'].split(' ')[:2])}...")

    def clear(self) -> None:
        self.main_ui.title.setText('')
        self.main_ui.note.setPlainText('')

    def delete_note(self, id_note: int):
        checkbox = QMessageBox.information(
            self, 'Notepad',
            'Вы действительно хотите удалить запись?',
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        if checkbox == 1024:
            data = self.readnotes()
            data.__delitem__(id_note)
            self.dump_note(data)
            if self.get_count_notes == 0:
                item = self.main_ui.notes.item(0)
                item.setText("Нет записей")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.note_window.close()
            else:
                self.main_ui.notes.takeItem(id_note)
                self.note_window.close()
        else:
            self.note_window.close()

    def edit(self, id_note: int):
        title, note = self.note_window.note_ui.title.text(), self.note_window.note_ui.note.toPlainText()
        if not title or not note:
            QMessageBox.warning(self, 'Notepad', 'Не все поля заполнены. Заполните все формы для сохранения!')
        else:
            data: list = self.readnotes()
            values = self.get_values()
            if title.lower() in values or note.lower() in values:
                QMessageBox.warning(self, 'Notepad', 'Заметка с таким заголовком или текстом уже существует!')
            else:
                data[id_note] = {'title': title, 'note': note, 'date': self.current_date}
                self.dump_note(data)
                self.main_ui.notes.item(id_note).setText(
                    f"{title.capitalize()}\n\n\n{self.current_date}\t{' '.join(note.split(' ')[:2])}...")
                self.note_window.close()


if __name__ == "__main__":
    application, main_window = QApplication(argv), Notepad()
    main_window.show()
    exit(application.exec())
