from PySide6.QtWidgets import QApplication, QMainWindow,QGridLayout,QHBoxLayout,QLineEdit,QLabel,QWidget,QComboBox,QPushButton,QVBoxLayout
import sys
from PySide6.QtCore import Qt


class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Create the main layout for the window
        self.grid_layout = QGridLayout()
        

        # Create a QHBoxLayout
        self.hbox_textbox = QHBoxLayout()
        # Create a QLabel and a QLineEdit
        self.label = QLabel('Label:')
        self.textbox = QLineEdit()
        self.textbox.setStyleSheet('font-size:30px; margin-right:100px; ')
        self.label.setStyleSheet('background-color:lightgray; font-size:30px; margin:20px;height:40px;')
        # Add the QLabel and QLineEdit to the QHBoxLayout
        self.hbox_textbox.addWidget(self.label)
        self.hbox_textbox.addWidget(self.textbox)
        # Add the QHBoxLayout to the grid layout
        self.grid_layout.addLayout(self.hbox_textbox, 0, 0)  # Add QHBoxLayout to row 0, column 0

        #layout fro dropdown
        self.hbox_dropdown=QHBoxLayout()
        self.label_dropdown=QLabel('Dropdown:')
        self.label_dropdown.setFixedWidth(256)
        self.combobox=QComboBox()
        self.combobox.setFixedWidth(400)
        self.combobox.addItems(["Option1","Option2","Option3"])
        self.label_dropdown.setStyleSheet('background-color:lightgray; font-size:30px;height:40px;width: 150px;')
        self.combobox.setStyleSheet('height:40px;width:100px;font-size:30px;')
        self.hbox_dropdown.addWidget(self.label_dropdown)
        self.hbox_dropdown.addWidget(self.combobox)
        self.grid_layout.addLayout(self.hbox_dropdown,1,0)

        #layout for button
        self.hbox_button=QHBoxLayout()
        self.Push_Button=QPushButton("Push Button")
        self.Push_Button.setStyleSheet('background-color:lightgray; font-size:30px; margin:20px;height:40px;width: 150px;')
        self.Push_Button.clicked.connect(self.on_push_button_clicked)
        self.hbox_button.addWidget(self.Push_Button)
        self.grid_layout.addLayout(self.hbox_button,3,0)

        #layout for tbx display
        self.tbxOutputgrid=QGridLayout()
        self.lbltextdisplay=QLineEdit()
        self.lbltextdisplay.setReadOnly(True)
        self.lbltextdisplay.setStyleSheet('background-color:white; font-size:30px;height:40px;width: 150px;')


        self.label_optextbx=QLabel("Textbox")
        self.label_optextbx.setFixedHeight(50)
        self.label_optextbx.setStyleSheet('background-color:lightgray; font-size:30px;height:40px;width: 150px;')

        self.tbop_vlayout=QVBoxLayout()
        self.tbop_vlayout.addWidget(self.label_optextbx)
        self.tbop_vlayout.addWidget(self.lbltextdisplay)

        self.tbxOutputgrid.addLayout(self.tbop_vlayout,0,0)

         #layout for cbx display
        self.lblcbxdisplay=QLineEdit()
        self.lblcbxdisplay.setReadOnly(True)
        self.lblcbxdisplay.setStyleSheet('background-color:white; font-size:30px;height:40px;width: 150px; text-align: center;')


        self.label_optexcbx=QLabel("Combobox")
        self.label_optexcbx.setFixedHeight(50)
        self.label_optexcbx.setStyleSheet('background-color:lightgray; font-size:30px;height:40px;width: 150px; text-align: center;')

        self.tbop_vlayout=QVBoxLayout()
        self.tbop_vlayout.addWidget(self.label_optexcbx)
        self.tbop_vlayout.addWidget(self.lblcbxdisplay)

        self.tbxOutputgrid.addLayout(self.tbop_vlayout,0,1)



        self.grid_layout.addLayout(self.tbxOutputgrid,4,0)

        self.lbldrpdwn=QLineEdit()
        self.lbldrpdwn.setReadOnly(True)





        self.setLayout(self.grid_layout)

        self.resize(1024,768)
        self.setWindowTitle('PySide6 Example')
        self.show()


    def on_push_button_clicked(self):
        # Handle the click event for the Push Button
        self.lblcbxdisplay.setText(self.combobox.currentText())
        self.lbltextdisplay.setText(self.textbox.text())     

        # Set the main layout for the window
if __name__ == "__main__":
    app = QApplication([])

    # Create and show the main window
    main_window = MyMainWindow()
    # main_window.show()

    app.exec()