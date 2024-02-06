import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton,QHeaderView
import csv

class MyTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a table widget
        self.tableWidget = QTableWidget(self)

        # Create a button to load CSV file
        self.loadButton = QPushButton('Load CSV', self)
        self.loadButton.clicked.connect(self.load_csv)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.loadButton)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def load_csv(self):
        # Open a file dialog to get the CSV file path
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setWindowTitle("Open CSV File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            # Read CSV file and populate the table
            self.populate_table_from_csv(file_path)

    def populate_table_from_csv(self, file_path):
        # Clear existing table content
        self.tableWidget.clear()

        # Read CSV file and get data as a list
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]

        # Set the number of rows and columns in the table
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        # Populate the table with data
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                self.tableWidget.setItem(i, j, item)
        
        self.tableWidget.verticalHeader().setVisible(False)

        # Remove horizontal header labels
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



def main():
    app = QApplication(sys.argv)

    window = MyTableWidget()
    window.showMaximized()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
