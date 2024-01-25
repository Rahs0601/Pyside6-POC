from PySide6.QtWidgets import *
from app1_MQTT import MQTT_Layout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout
        self.mainlayout = QGridLayout(self)

        # Create the second widget (row) to fill the remaining space
        self.remaining_space_widget = QHBoxLayout()
        self.mainlayout.addLayout(self.remaining_space_widget,0,0)



        # Create the first widget (row) with a specific height
        self.horizontal_layout=QHBoxLayout()
        self.btn_mqtt = QPushButton("MQTT")
        self.btn_pdfview = QPushButton("PDF Reader")
        self.btn_Excelview = QPushButton("Excel Viewer")
        self.btn_Graph = QPushButton("Graph and PieChart")
        self.btn_Sql = QPushButton("SQL")


        self.btn_mqtt.clicked.connect(self.on_mqtt_clicked)

        self.horizontal_layout.addWidget(self.btn_mqtt)
        self.horizontal_layout.addWidget(self.btn_pdfview)
        self.horizontal_layout.addWidget(self.btn_Excelview)
        self.horizontal_layout.addWidget(self.btn_Graph)
        self.horizontal_layout.addWidget(self.btn_Sql)

        self.mainlayout.addLayout(self.horizontal_layout,1,0)

        # Set the layout for the main widget
        self.setLayout(self.mainlayout)

    def on_mqtt_clicked(self):
        self.clearLayout(self.remaining_space_widget)

        # Add new layout
        mqtt=MQTT_Layout()
        self.remaining_space_widget.addWidget(mqtt)
        print('efwv')



    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

       
if __name__ == "__main__":
    app = QApplication([])
    window = MyWidget()
    window.showMaximized()
    app.exec()
