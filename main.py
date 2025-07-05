from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QPushButton
from PyQt5 import uic
import sys
import random
import string


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi('password_generator.ui', self)
        self.setWindowTitle('Password Generator!')

        # Define Our Widgets
        self.generate_button = self.findChild(QPushButton, 'generate_pushButton')
        self.copy_button = self.findChild(QPushButton, 'copy_pushButton')
        self.pwlabel = self.findChild(QLabel, 'passwordlabel')
        self.header = self.findChild(QLabel, 'headerlabel')
        self.lineEdit = self.findChild(QLineEdit, 'lineEdit')

        # Click The Button
        self.generate_button.clicked.connect(self.generate)
        self.copy_button.clicked.connect(self.copy)

        # Show The App
        self.show()

    def generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password_length = int(self.lineEdit.text())
        password = ''.join(random.sample(characters, k=password_length))
        self.pwlabel.setText(password)
        self.lineEdit.setText('')

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.pwlabel.text())


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
