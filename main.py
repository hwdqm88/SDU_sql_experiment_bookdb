from PySide6.QtWidgets import QApplication
from widget.mainwindow import MainWindow
from lib.share import SI
from database.connector import Connector

if __name__ == '__main__':
    app = QApplication([])
    widget = MainWindow(None)
    widget.show()
    app.exec()
    Connector.close_connection()
