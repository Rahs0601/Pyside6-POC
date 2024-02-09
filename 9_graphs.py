from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import sys
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the main widget and set its layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout(central_widget)

        data = pd.read_csv('PerformanceData_20240206.csv')
        performance = data['% Processor Time']
        system_calls = data['System Calls/sec']

        # Create the figure and axis objects
        fig1 = Figure()
        ax1 = fig1.add_subplot(111)
        ax1.hist(performance, bins=100)
        ax1.set_ylabel('Performance')
        ax1.set_xlabel('0-100')
        canvas1 = FigureCanvasQTAgg(fig1)
        self.grid_layout.addWidget(canvas1, 0, 0)

        fig2 = Figure()
        ax2 = fig2.add_subplot(111)
        ax2.hist(system_calls, bins=3)
        ax2.set_ylabel('System Calls/sec')
        ax2.set_xlabel('0-100')
        canvas2 = FigureCanvasQTAgg(fig2)
        self.grid_layout.addWidget(canvas2, 0, 1)


if __name__ == "__main__":
    app = QApplication([])

    # Create and show the main window
    main_window = MyMainWindow()
    main_window.resize(1024, 768)
    main_window.setWindowTitle('PySide6 Example')
    main_window.show()

    sys.exit(app.exec())
