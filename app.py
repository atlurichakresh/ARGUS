import sys
from PySide6.QtWidgets import QApplication
from argus.ui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ARGUS 4.3")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
