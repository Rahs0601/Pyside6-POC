import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Import the generated UI file
from UserDemo2 import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect button clicks to respective functions
        self.pushButton.clicked.connect(self.show_dashboard)
        self.pushButton_2.clicked.connect(self.show_pdf_viewer)
        self.pushButton_3.clicked.connect(self.show_excel_viewer)
        self.pushButton_4.clicked.connect(self.show_graph_elements)
        self.pushButton_6.clicked.connect(self.show_sql)
        self.pushButton_5.clicked.connect(self.HideMenu)
        self.pushButton_5.setCheckable(True)

    def show_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_pdf_viewer(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_excel_viewer(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_graph_elements(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_sql(self):
        self.stackedWidget.setCurrentIndex(4)

    def HideMenu(self):
        if self.pushButton_5.isChecked():
            self.frame.setFixedWidth(0)
        else:
            self.frame.setFixedWidth(225)
           

       

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
