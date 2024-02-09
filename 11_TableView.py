from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget,QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self,parent):
        return len(self._data)

    def columnCount(self,parent):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._data[row][col]
            return str(value)
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        data = [
            [1, 'John', 'Doe'],
            [2, 'Jane', 'Smith'],
            [3,'Mike','Bob']
        ]

        table_model = MyTableModel(data)
        table_view = QTableView()
        table_view.verticalHeader().setVisible(False)

        # Remove horizontal header labels
        table_view.horizontalHeader().setVisible(False)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.setModel(table_model)

        self.layout.addWidget(table_view)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
