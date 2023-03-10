# Form implementation generated from reading ui file '.\Notepad.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtGui, QtWidgets, QtCore

from config import NotepadConfig
from qrc import res  # type: ignore


class UiNotepad(object):
    def setup_ui(self, Notepad):
        Notepad.setObjectName("Notepad")
        Notepad.setFixedSize(440, 650)
        favicon = QtGui.QIcon()
        favicon.addPixmap(QtGui.QPixmap(
                ":/icons/C:/Users/Ryzen/PycharmProjects/notepad/notepad/icons/description_black_24dp.svg"),
                QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Notepad.setWindowIcon(favicon)
        self.centralwidget = QtWidgets.QWidget(parent=Notepad)
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QFrame(parent=self.centralwidget)
        self.main.setGeometry(QtCore.QRect(-1, 0, 440, 650))
        self.main.setStyleSheet("QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255),stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Rubik, sans-serif;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}")
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.layoutWidget = QtWidgets.QWidget(parent=self.main)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 420, 600))
        self.layoutWidget.setObjectName("layoutWidget")
        self.frames = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.frames.setContentsMargins(0, 0, 0, 0)
        self.frames.setObjectName("frames")
        self.body = QtWidgets.QFrame(parent=self.layoutWidget)
        self.body.setStyleSheet("QFrame {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"color: white;\n"
"}")
        self.body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.body.setObjectName("body")
        self.save = QtWidgets.QPushButton(parent=self.body)
        self.save.setGeometry(QtCore.QRect(10, 255, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setBold(True)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.save.setObjectName("save")
        self.delete_note = QtWidgets.QPushButton(parent=self.body)
        self.delete_note.setGeometry(QtCore.QRect(370, 254, 30, 30))
        self.delete_note.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        delete_icon = QtGui.QIcon()
        delete_icon.addPixmap(QtGui.QPixmap(
            ":/icons/C:/Users/Ryzen/PycharmProjects/notepad/notepad/icons/delete_white_24dp.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_note.setIcon(delete_icon)
        self.delete_note.setIconSize(QtCore.QSize(24, 24))
        self.delete_note.setObjectName("delete_note")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.body)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 400, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.create = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.create.setContentsMargins(0, 0, 0, 0)
        self.create.setSpacing(6)
        self.create.setObjectName("create")
        self.title = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Rubik, sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet("QLineEdit {border-radius: 7px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; font-size: 20px; color: white; background-color: rgba(255, 255, 255, 30);}")
        self.title.setMaxLength(25)
        self.title.setObjectName("title")
        self.create.addWidget(self.title)
        self.note = QtWidgets.QPlainTextEdit(parent=self.layoutWidget1)
        self.note.setFont(font)
        self.note.setStyleSheet("border: none; border-top-left-radius: 0px; border-top-right-radius: 0px; font-size: 14px;")
        self.note.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.note.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.note.setObjectName("note")
        self.create.addWidget(self.note)
        self.frames.addWidget(self.body)
        self.footer = QtWidgets.QFrame(parent=self.layoutWidget)
        self.footer.setStyleSheet("background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px;")
        self.footer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.footer.setObjectName("footer")
        self.notes = QtWidgets.QListWidget(parent=self.footer)
        self.notes.setGeometry(QtCore.QRect(4, 4, 410, 290))
        self.notes.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.notes.setStyleSheet("QListWidget{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"width: 390px;\n"
"height: 100px;\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}")
        self.notes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notes.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.notes.setProperty("isWrapping", False)
        self.notes.setSpacing(16)
        self.notes.setObjectName("notes")
        self.font_notes = QtGui.QFont()
        self.font_notes.setFamily("Rubik")
        self.font_notes.setPointSize(14)
        self.font_notes.setWeight(50)
        self.cfg = NotepadConfig()
        if self.cfg.get_count_notes == 0:
            item = QtWidgets.QListWidgetItem()
            item.setFont(self.font_notes)
            self.notes.addItem(item)
        else:
            for _ in range(self.cfg.get_count_notes):
                item = QtWidgets.QListWidgetItem()
                item.setFont(self.font_notes)
                self.notes.addItem(item)
        self.frames.addWidget(self.footer)
        self.close = QtWidgets.QPushButton(parent=self.main)
        self.close.setGeometry(QtCore.QRect(402, 4, 30, 30))
        self.close.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        close_icon = QtGui.QIcon()
        close_icon.addPixmap(QtGui.QPixmap(
                ":/icons/C:/Users/Ryzen/PycharmProjects/notepad/notepad/icons/close_white_24dp.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close.setIcon(close_icon)
        self.close.setIconSize(QtCore.QSize(24, 24))
        self.close.setObjectName("close")
        self.logo_title = QtWidgets.QLabel(parent=self.main)
        self.logo_title.setGeometry(QtCore.QRect(160, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik,sans-serif")
        font.setBold(True)
        font.setPointSize(21)
        self.logo_title.setFont(font)
        self.logo_title.setStyleSheet("background-color: none;")
        self.logo_title.setObjectName("logo_title")
        self.logo = QtWidgets.QPushButton(parent=self.main)
        self.logo.setGeometry(QtCore.QRect(5, 5, 31, 31))
        self.logo.setStyleSheet("border: none;")
        logo_icon = QtGui.QIcon()
        logo_icon.addPixmap(QtGui.QPixmap(
                ":/icons/C:/Users/Ryzen/PycharmProjects/notepad/notepad/icons/description_white_24dp.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logo.setIcon(logo_icon)
        self.logo.setIconSize(QtCore.QSize(24, 24))
        self.logo.setObjectName("logo")
        Notepad.setCentralWidget(self.centralwidget)

        self.retranslate_ui(Notepad)
        QtCore.QMetaObject.connectSlotsByName(Notepad)

    def retranslate_ui(self, Notepad):
        _translate = QtCore.QCoreApplication.translate
        Notepad.setWindowTitle(_translate("Notepad", "Notepad"))
        self.save.setText(_translate("Notepad", "Сохранить"))
        self.save.setShortcut(_translate("Notepad", "Return"))
        self.delete_note.setShortcut(_translate("Notepad", "Del"))
        self.title.setPlaceholderText(_translate("Notepad", "Заголовок"))
        self.note.setPlaceholderText(_translate("Notepad", "Запись"))
        __sortingEnabled = self.notes.isSortingEnabled()
        self.notes.setSortingEnabled(False)
        if self.cfg.get_count_notes == 0:
            item = self.notes.item(0)
            item.setText("Нет записей")
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            for i, e in enumerate(self.cfg.readnotes()):
                item = self.notes.item(i)
                data = tuple(e.values())
                item.setText(f"{data[0].title()}\n\n\n{data[2]}\t{' '.join(data[1].split(' ')[:2])}...")
        self.notes.setSortingEnabled(__sortingEnabled)
        self.logo_title.setText(_translate("Notepad", "Notepad"))
