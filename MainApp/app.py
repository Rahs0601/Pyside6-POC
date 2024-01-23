from argparse import ArgumentParser, RawTextHelpFormatter
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import paho.mqtt.client as mqtt
# import pdfviewer as pdfviewer
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl, QCoreApplication
from MainApp.pdfviewer.main import PDFViewer
# from PDFViewer import PDFViewer
# from mainwindow import MainWindow
# from pdfviewer import main as 
# from zoomselector import ZoomSelector
# from ui_mainwindow import Ui_MainWindow
import threading

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 400, 300)
        #create Label
        txt = "";
        self.label = QLabel(self)
        self.label.move(50, 50)
        self.label.resize(200, 30)
        self.label.setText(txt)


        # Create buttons
        mqtt_button = QPushButton("Subscribe to MQTT", self)
        mqtt_button.setGeometry(50, 50, 300, 30)
        mqtt_button.clicked.connect(self.subscribe_to_mqtt)

        pdf_button = QPushButton("View PDF", self)
        pdf_button.setGeometry(50, 100, 300, 30)
        pdf_button.clicked.connect(self.view_pdf)

        excel_csv_button = QPushButton("View Excel CSV", self)
        excel_csv_button.setGeometry(50, 150, 300, 30)
        excel_csv_button.clicked.connect(self.view_excel_csv)

        api_button = QPushButton("Test Web API", self)
        api_button.setGeometry(50, 200, 300, 30)
        api_button.clicked.connect(self.test_web_api)

        sqlite_button = QPushButton("Connect and Read SQLite Data", self)
        sqlite_button.setGeometry(50, 250, 300, 30)
        sqlite_button.clicked.connect(self.connect_read_sqlite)

        mssql_button = QPushButton("Connect and Read MSSQL Data", self)
        mssql_button.setGeometry(50, 300, 300, 30)
        mssql_button.clicked.connect(self.connect_read_mssql)

        google_button = QPushButton("Login using Google", self)
        google_button.setGeometry(50, 350, 300, 30)
        google_button.clicked.connect(self.login_google)

    def on_message(client, userdata, msg):
            print(f"Received message: {msg.payload.decode()}")
            txt = msg.payload.decode()

    def Mqtt_subscribe(self):
        import paho.mqtt.client as mqtt
        # Define the MQTT broker and topic
        broker_address = "127.0.0.1"
        topic = "HMI-To-Service-Topic"

        # Callback when a message is received
        def on_message(client, userdata, msg):
            print(f"Received message: {msg.payload.decode()}")

        # Create an MQTT client instance
        client = mqtt.Client("Subscriber")

        # Set the on_message callback
        client.on_message = on_message

        # Connect to the broker
        client.connect(broker_address)

        # Subscribe to the specified topic
        client.subscribe(topic)

        # Keep the script running to receive messages
        client.loop_forever()

    def subscribe_to_mqtt(self):
        thread = threading.Thread(target=self.Mqtt_subscribe)
        thread.start()
    
    def view_pdf(self):
        PDFViewer.main()
    def view_excel_csv(self):
        # TODO: Implement Excel CSV viewing logic
        pass

    def test_web_api(self):
        # TODO: Implement web API testing logic
        pass

    def connect_read_sqlite(self):
        # TODO: Implement SQLite connection and data reading logic
        pass

    def connect_read_mssql(self):
        # TODO: Implement MSSQL connection and data reading logic
        pass

    def login_google(self):
        # TODO: Implement Google login logic
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
