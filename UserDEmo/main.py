import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Import the generated UI file
from UserDemo2 import Ui_MainWindow
import pandas as pd
from sqlalchemy import create_engine
connection_string = r"mssql+pyodbc://sa:pctadmin$1234@WIN10-TEST\SQLEXPRESS2019/BASELINE?driver=ODBC Driver 17 for SQL Server"
engine = create_engine(connection_string)
def gettable():
    # Create a SQLAlchemy engine
    sql_query = 'SELECT table_name = t.name FROM sys.tables t INNER JOIN sys.schemas s ON t.schema_id = s.schema_id'

    # Use pandas to read data from SQL into a DataFrame
    df = pd.read_sql(sql_query, engine)



    # Perform any data manipulation or analysis as needed on the DataFrame

    # Save the DataFrame back to SQL (replace 'new_table' with your desired table name)
    # df.to_sql(name='new_table', con=engine, index=False, if_exists='replace')
    # df.to_csv('MachineInformation.csv', index=False)
    # print(f'Data has been successfully exported to MachineInformation.csv')
    # Close the SQLAlchemy engine
    engine.dispose()
    return list(df['table_name'])

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
        # autowidth
        
        self.comboBox.addItems(gettable())
        

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
