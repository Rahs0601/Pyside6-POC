import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import pandas as pd

class CSVViewer(QMainWindow):
    def __init__(self, file_path):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)

        self.load_csv(file_path)

    def load_csv(self, file_path):
        try:
            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv(file_path)

            # Get the number of rows and columns in the DataFrame
            rows, cols = df.shape

            # Set the number of rows and columns in the QTableWidget
            self.table_widget.setRowCount(rows)
            self.table_widget.setColumnCount(cols)

            # Set the header labels
            self.table_widget.setHorizontalHeaderLabels(df.columns.astype(str))

            # Populate the QTableWidget with data from the DataFrame
            for row in range(rows):
                for col in range(cols):
                    item = QTableWidgetItem(str(df.iloc[row, col]))
                    self.table_widget.setItem(row, col, item)

            # Auto-resize columns to fit content
            self.table_widget.resizeColumnsToContents()

        except Exception as e:
            print(f"Error loading CSV file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/your/file.csv")
        sys.exit(1)

    file_path = "productionData.csv";

    app = QApplication(sys.argv)
    window = CSVViewer(file_path)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
