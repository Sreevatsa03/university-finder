import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
from university_finder_app import UniversityFinder

qtcreator_file = "ui_files/universities_access_db.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class UniversityFinderUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.university_finder = UniversityFinder()

        # run functions
        self.access_db_button.clicked.connect(self.enter_app)
        self.shutdown_db_button.clicked.connect(self.exit_app)
    
    def enter_app(self):
        user = str(self.username_box.toPlainText())
        password = str(self.password_box.toPlainText())
        self.university_finder.authenticate(user, password)

    def exit_app(self):
        self.university_finder.shutdown()
        self.close()


def main():
    app = QApplication(sys.argv)
    window = UniversityFinderUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()