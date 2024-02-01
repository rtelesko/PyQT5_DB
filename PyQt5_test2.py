# Adapted from https://realpython.com/python-pyqt-database/#navigating-the-records-in-a-query
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
)


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(415, 200)
        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("contacts")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Job")
        self.model.setHeaderData(3, Qt.Horizontal, "Email")
        # Querying
        # (1) Returning all rows
        self.model.select()
        # (3) Filtering
        # self.model.setFilter("ID = 2")
        # self.model.select()
        # (3) Custom SQL statements
        # self.model.setQuery(QSqlQuery("SELECT * FROM contacts WHERE ID = 1"))
        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


def create_connection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


app = QApplication(sys.argv)
if not create_connection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec_())
