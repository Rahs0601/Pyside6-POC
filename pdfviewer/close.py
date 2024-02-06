from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.setWindowTitle("Close Event Example")
    widget.resize(400, 300)
    widget.show()

    app.exec()
