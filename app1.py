from PySide6.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout
        self.layout = QVBoxLayout(self)

        # Create the second widget (row) to fill the remaining space
        remaining_space_widget = QLabel("Second Row (Fill Remaining Space)")
        self.layout.addWidget(remaining_space_widget)

        # Create the first widget (row) with a specific height
        self.horizontal_layout=QHBoxLayout()
        self.btn_mqtt = QPushButton("MQTT")
        self.btn_pdfview = QPushButton("PDF Reader")
        self.btn_Excelview = QPushButton("Excel Viewer")
        self.btn_Graph = QPushButton("Graph and PieChart")
        self.btn_Sql = QPushButton("SQL")

        self.layout.addWidget(self.btn_mqtt)
        self.layout.addWidget(self.btn_pdfview)
        self.layout.addWidget(self.btn_Excelview)
        self.layout.addWidget(self.btn_Graph)
        self.layout.addWidget(self.btn_Sql)

        # Set the layout for the main widget
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec()
