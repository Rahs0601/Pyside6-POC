import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import json
import requests
from googleapiclient.discovery import build


class GoogleLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.login_button = QPushButton("Login with Google", self)
        self.login_button.clicked.connect(self.handle_login)
        self.layout.addWidget(self.login_button)

        self.credentials = None

    def handle_login(self):
        # Set up the OAuth 2.0 flow for Google login
        flow = InstalledAppFlow.from_client_secrets_file(
            r"Cltscrt\client_secret_433522196327-u3t1gk7d5777lqo5bfuiaomdc3o5m1vb.apps.googleusercontent.com.json",  # Replace with your client secret file
            scopes=['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/userinfo.profile']
        )

        # Run the OAuth 2.0 authorization flow
        self.credentials = flow.run_local_server(port=0)

        # After successful authentication, you can use the 'self.credentials' object to make API requests
        # For example, print the access token
        print("Access Token:", self.credentials.token)
        # print(name)
        service = build('people', 'v1', credentials=self.credentials)
        profile = service.people().get(resourceName='people/me', personFields='names').execute()

        # Print the name of the authenticated user
        # print("User Name:", user_info['emailAddress'])
        names = profile.get('names', [])
        if names:
            print("User Name:", names[0].get('displayName'))
        print(names)
            
    def closeEvent(self, event):
        pass
        # if self.credentials:
            # # Save the credentials to a file for future use
            # self.credentials.to_json_file('token.json')

if __name__ == "__main__":
    # client_secret = 
    app = QApplication(sys.argv)
    window = GoogleLoginWindow()
    window.show()
    sys.exit(app.exec())
