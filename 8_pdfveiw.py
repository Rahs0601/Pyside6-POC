import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHeaderView
import fitz  # PyMuPDF

class MyTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a table widget
        self.tableWidget = QTableWidget(self)

        # Create a button to load PDF file
        self.loadButton = QPushButton('Load PDF', self)
        self.loadButton.clicked.connect(self.load_pdf)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.loadButton)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def load_pdf(self):
        # Open a file dialog to get the PDF file path
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setWindowTitle("Open PDF File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            # Read PDF file and populate the table
            self.populate_table_from_pdf(file_path)

    def populate_table_from_pdf(self, file_path):
        # Open PDF file
        doc = fitz.open(file_path)

        # Clear existing table content
        self.tableWidget.clear()

        # Get number of pages
        num_pages = doc.page_count

        # Set the number of rows and columns in the table
        self.tableWidget.setRowCount(num_pages)
        self.tableWidget.setColumnCount(1)

        # Populate the table with text content from each page
        for i in range(num_pages):
            page = doc.load_page(i)
            text = page.get_text()
            item = QTableWidgetItem(text)
            self.tableWidget.setItem(i, 0, item)

        # Adjust column width
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

def main():
    app = QApplication(sys.argv)

    window = MyTableWidget()
    window.showMaximized()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
