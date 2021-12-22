from rootWidget import rootWidget
from PySide2.QtWidgets import QApplication
import sys
from lib.share import SI
if __name__ == "__main__":
    app = QApplication([])
    SI.rootWidget = rootWidget()
    SI.rootWidget.show()
    sys.exit(app.exec_())