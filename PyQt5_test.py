import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("my_ui.ui", self)

        # Find the widgets in the xml file
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.clicked_btn)
        self.show()

    def clicked_btn(self):
        self.textedit.append("This is a test!")


app = QApplication(sys.argv)
window = UI()
app.exec_()
