import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QStackedWidget

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Username:", self))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:", self))
        layout.addWidget(self.password_input)

class MainAppWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.logout_button = QPushButton("Logout", self) 
        self.logout_button.clicked.connect(parent.handle_logout)
        layout.addWidget(QLabel("Main App"))
        layout.addWidget(self.logout_button)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Demo")
        self.setGeometry(100, 100, 400, 300)

        self.stacked_widget = QStackedWidget(self)
        self.login_widget = LoginWidget(self)
        self.main_app_widget = MainAppWidget(self)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.main_app_widget)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.handle_login)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.login_button)

    def handle_login(self):
        # Perform login authentication here
        # For demo, just switch to main app widget
        self.stacked_widget.setCurrentWidget(self.main_app_widget)

    def handle_logout(self):
        print("Logout")
        self.stacked_widget.setCurrentWidget(self.login_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
