# main.py
import sys
from PyQt5.QtWidgets import QApplication
from login_ui import LoginWindow
from stylesheet import STYLE_SHEET

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)
    
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())