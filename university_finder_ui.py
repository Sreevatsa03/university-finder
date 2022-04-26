import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from university_finder_app import UniversityFinder

ui_1 = "ui_files/universities_access_db.ui"
AccessWindow, QtBaseClass = uic.loadUiType(ui_1)

ui_2 = "ui_files/search_or_watchlist.ui"
Search_WatchlistWindow, QtBaseClass = uic.loadUiType(ui_2)


class AccessDB(QMainWindow, AccessWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        AccessWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.university_finder = UniversityFinder()

        # run functions
        self.access_db_button.clicked.connect(self.enter_app)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def enter_app(self):
        """ Authenticate username and password to enter application """

        # authenticate username and password
        user = str(self.username_box.toPlainText())
        password = str(self.password_box.toPlainText())
        self.university_finder.authenticate(user, password)

        # open new window
        self.search_or_watchlist = Search_or_Watchlist(self.university_finder)
        self.search_or_watchlist.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.close()


class Search_or_Watchlist(QMainWindow, Search_WatchlistWindow):

    def __init__(self, university_finder):
        QMainWindow.__init__(self)
        Search_WatchlistWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.university_finder = university_finder

        # run functions
        self.search_button.clicked.connect(self.search_universities)
        # self.watchlist_button.clicked.connect(self.search_universities)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def search_universities(self):
        """ Show list of all universities. Open window to filter results. """

        # get df of results from query
        df = self.university_finder.show_universities()
        # print(df)

        # view dataframe
        self.model = pandasModel(df)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resize(800, 600)
        self.view.show()

    def access_watchlist(self):
        pass

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.close()


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


def main():
    app = QApplication(sys.argv)
    window = AccessDB()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
