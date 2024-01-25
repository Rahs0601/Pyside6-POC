# layout.py
from PySide6.QtWidgets import *

class MQTT_Layout(QWidget):
    def __init__(self):
        super().__init__()

    # def get_layout():
        self.layout = QGridLayout()

        self.recvd_msg_layout=QHBoxLayout()
        self.lblrecvd_msg=QLabel("MQTT Recived Message")
        self.recvd_msg_layout.addWidget(self.lblrecvd_msg)
        self.lblrecvd_msg.setStyleSheet('font-size:30px;')

        self.tbx_recvd_message=QLineEdit()
        self.tbx_recvd_message.setReadOnly(True)
        self.tbx_recvd_message.setStyleSheet('font-size:30px;')
        self.recvd_msg_layout.addWidget(self.tbx_recvd_message)
        self.layout.addLayout(self.recvd_msg_layout,0,0)

        self.publish_msg_layout=QHBoxLayout()
        self.tbx_message=QLineEdit()
        self.tbx_message.setStyleSheet('font-size:30px;')
        self.publish_msg_layout.addWidget(self.tbx_message)

        self.btn_publish=QPushButton("PUBLISH")
        self.publish_msg_layout.addWidget(self.btn_publish)
        self.btn_publish.setStyleSheet('font-size:30px;margin:20px;width:200px')
        self.btn_publish.clicked.connect(self.on_publish_click)

        self.layout.addLayout(self.publish_msg_layout,1,0)

        self.setLayout(self.layout)

    def on_publish_click(self):
        print(self.tbx_message.text())

        # return self.layout
        
