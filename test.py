from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def main():
    app = QApplication([])

    # Create a QWidget to hold the button
    widget = QWidget()

    # Create a vertical layout
    layout = QVBoxLayout(widget)

    # Create a QPushButton
    button = QPushButton("Click Me")
    button.setCheckable(True)  # 'True' should be capitalized

    # Add the button to the layout
    layout.addWidget(button)

    # Set the style sheet of the button to change colors on press and release
    button.setStyleSheet(
        '''
        QPushButton {
            background-color: red;
            border: none;
            padding: 10px;
            color: white;
        }
        QPushButton:checked {
            background-color: green;
        }
        '''
    )

    # Show the widget
    widget.show()

    # Execute the application
    app.exec()

if __name__ == '__main__':
    main()
