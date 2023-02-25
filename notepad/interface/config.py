from json import load, dump
from os import getenv, path, mkdir
from datetime import datetime


class NotepadConfig:
    note_dir, fullpath = f'{getenv("tmp")}/notepad/', f'{getenv("tmp")}/notepad/data.json'

    def __init__(self):
        if not path.exists(self.note_dir):
            mkdir(self.note_dir)
        if not path.exists(self.fullpath):
            self.dump_note([])

    def dump_note(self, data: list) -> None:
        with open(self.fullpath, 'w', encoding='utf-8') as writer:
            dump(data, writer, ensure_ascii=False, indent=4)

    def readnotes(self) -> list:
        with open(self.fullpath, encoding='utf-8') as read_file:
            return load(read_file)

    def get_values(self):
        return (value.lower() for e in self.readnotes() for value in tuple(e.values())[:2])

    @staticmethod
    def append_data(__obj: list, title: str, note: str) -> None:
        __obj.append({'title': title, 'note': note, 'date': datetime.now().strftime('%d.%m.%Y')})

    @property
    def get_count_notes(self) -> int:
        return len(self.readnotes())
