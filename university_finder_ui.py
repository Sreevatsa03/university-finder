import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from university_finder_app import UniversityFinder

ui_1 = "ui_files/universities_access_db.ui"
AccessWindow, QtBaseClass = uic.loadUiType(ui_1)

ui_2 = "ui_files/search_or_watchlist.ui"
Search_WatchlistWindow, QtBaseClass = uic.loadUiType(ui_2)

ui_3 = "ui_files/search.ui"
SearchWindow, QtBaseClass = uic.loadUiType(ui_3)

ui_4 = "ui_files/filter.ui"
FilterWindow, QtBaseClass = uic.loadUiType(ui_4)

ui_5 = "ui_files/add_to_watchlist.ui"
AddWatchlistWindow, QtBaseClass = uic.loadUiType(ui_5)

ui_6 = "ui_files/locations.ui"
LocationsWindow, QtBaseClass = uic.loadUiType(ui_6)

ui_7 = "ui_files/reviews.ui"
ReviewsWindow, QtBaseClass = uic.loadUiType(ui_7)

ui_8 = "ui_files/write_review.ui"
WriteReviewWindow, QtBaseClass = uic.loadUiType(ui_8)

ui_9 = "ui_files/watchlist.ui"
WatchlistWindow, QtBaseClass = uic.loadUiType(ui_9)

ui_10 = "ui_files/edit_notes.ui"
EditNotesWindow, QtBaseClass = uic.loadUiType(ui_10)

ui_11 = "ui_files/remove_from_watchlist.ui"
RemoveWatchlistWindow, QtBaseClass = uic.loadUiType(ui_11)


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
        self.search_or_watchlist = SearchorWatchlist(
            user, password, self.university_finder)
        self.search_or_watchlist.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.close()


class SearchorWatchlist(QMainWindow, Search_WatchlistWindow):

    def __init__(self, user, password, university_finder):
        QMainWindow.__init__(self)
        Search_WatchlistWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # run functions
        self.search_button.clicked.connect(self.search_universities)
        self.watchlist_button.clicked.connect(self.access_watchlist)
        self.review_button.clicked.connect(self.write_review)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def search_universities(self):
        """ Show list of all universities. Open window to filter results. """

        # get df of results from query
        df = self.university_finder.show_universities()

        # view dataframe
        self.model = pandasModel(df)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resize(800, 500)
        self.view.show()

        # change windows to search window
        self.search = Search(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def access_watchlist(self):
        """ Access watchlist """

        # get dataframe
        df = self.university_finder.show_watchlist()

        # view dataframe
        self.watch_model = pandasModel(df)
        self.watch_view = QTableView()
        self.watch_view.setModel(self.watch_model)
        self.watch_view.resize(600, 500)
        self.watch_view.show()

        # change windows to search window
        self.watch = Watchlist(self.user, self.password,
                                  self.university_finder, self.watch_model, self.watch_view)
        self.watch.show()
        self.close()

    def write_review(self):
        """ Write review """

        # get dataframe
        df = self.university_finder.show_reviews()

        # view dataframe
        self.rev_model = pandasModel(df)
        self.rev_view = QTableView()
        self.rev_view.setModel(self.rev_model)
        self.rev_view.resize(600, 500)
        self.rev_view.show()

        # change windows to search window
        self.review = WriteReview(self.user, self.password,
                                  self.university_finder, self.rev_model, self.rev_view)
        self.review.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.close()


class Watchlist(QMainWindow, WatchlistWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        WatchlistWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.add_to_watchlist_button.clicked.connect(self.add_to_watchlist)
        self.edit_notes_button.clicked.connect(self.edit_notes)
        self.remove_button.clicked.connect(self.remove_from_watchlist)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def add_to_watchlist(self):
        """ Add university to watchlist """

        # get dataframe
        df = self.university_finder.show_universities()

        # close table view
        self.view.close()

        # view dataframe
        self.all_model = pandasModel(df)
        self.all_view = QTableView()
        self.all_view.setModel(self.all_model)
        self.all_view.resize(800, 500)
        self.all_view.show()

        # change windows to add_to_watchlist window
        self.watchlist = AddtoWatchlist(
            self.user, self.password, self.university_finder, self.all_model, self.all_view)
        self.watchlist.show()
        self.university_finder.shutdown()
        self.close()

    def edit_notes(self):
        """ Edit notes of university in watchlist """
        
        # open edit notes window
        self.notes = EditNotes(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.notes.show()
        self.close()

    def remove_from_watchlist(self):
        """ Remove university from watchlist """

        # open edit notes window
        self.remove = RemovefromWatchlist(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.remove.show()
        self.close()

    def go_back(self):
        """ Go to previous window """

        # close table view
        self.view.close()

        # open previous window obj
        self.search_or_watchlist = SearchorWatchlist(
            self.user, self.password, self.university_finder)
        self.search_or_watchlist.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class EditNotes(QMainWindow, EditNotesWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        EditNotesWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.edit_notes_button.clicked.connect(self.edit_notes)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def edit_notes(self):
        """ Add university to watchlist """

        name = str(self.name_box.toPlainText())
        notes = str(self.notes_box.toPlainText())
        self.university_finder.edit_notes(name, notes)

        # close view and open new view of watchlist
        self.view.close()

        df = self.university_finder.show_watchlist()
        self.watchlist_model = pandasModel(df)
        self.watchlist_view = QTableView()
        self.watchlist_view.setModel(self.watchlist_model)
        self.watchlist_view.resize(800, 500)
        self.watchlist_view.show()

    def go_back(self):
        """ Go to previous window """

        # open previous window obj
        self.watchlist = Watchlist(self.watchlist_user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class RemovefromWatchlist(QMainWindow, RemoveWatchlistWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        RemoveWatchlistWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.remove_button.clicked.connect(self.remove_from_watchlist)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def remove_from_watchlist(self):
        """ Add university to watchlist """

        name = str(self.name_box.toPlainText())
        self.university_finder.remove_from_watchlist(name)

        # close view and open new view of watchlist
        self.view.close()

        df = self.university_finder.show_watchlist()
        self.watchlist_model = pandasModel(df)
        self.watchlist_view = QTableView()
        self.watchlist_view.setModel(self.watchlist_model)
        self.watchlist_view.resize(800, 500)
        self.watchlist_view.show()

    def go_back(self):
        """ Go to previous window """

        # open previous window obj
        self.watchlist = Watchlist(self.watchlist_user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class WriteReview(QMainWindow, WriteReviewWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        WriteReviewWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.write_review_button.clicked.connect(self.write_review)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def write_review(self):
        """ Write review """

        # get dataframe
        rating = str(self.rating_box.value())
        name = str(self.name_box.toPlainText())
        description = str(self.description_box.toPlainText())
        df = self.university_finder.write_review(rating, description, self.user, name)

        # close table view
        self.view.close()

        # get new dataframe
        df = self.university_finder.show_reviews()

        # view new dataframe
        self.rev_model = pandasModel(df)
        self.rev_view = QTableView()
        self.rev_view.setModel(self.rev_model)
        self.rev_view.resize(600, 500)
        self.rev_view.show()

    def go_back(self):
        """ Go to previous window """

        # close table view
        self.view.close()

        # open previous window obj
        self.search_or_watchlist = SearchorWatchlist(
            self.user, self.password, self.university_finder)
        self.search_or_watchlist.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class Search(QMainWindow, SearchWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        SearchWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.filter_uni_button.clicked.connect(self.filter_universities)
        self.search_name_button.clicked.connect(
            self.search_universities_by_name)
        self.search_code_button.clicked.connect(
            self.search_universities_by_code)
        self.search_loc_button.clicked.connect(self.search_locations)
        self.search_review_button.clicked.connect(self.search_reviews)
        self.view_club_button.clicked.connect(self.view_clubs)
        self.view_alumn_button.clicked.connect(self.view_alumni)
        self.view_dep_button.clicked.connect(self.view_departments)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def filter_universities(self):
        """ Open window to filter universities """

        # change windows to filter window
        self.filter = Filter(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.filter.show()
        self.close()

    def search_universities_by_name(self):
        """ Search for university based on name """

        # get user-inputted name and call procedure
        name = str(self.name_box.toPlainText())
        df = self.university_finder.search_universities_by_name(name)

        # view dataframe
        self.name_model = pandasModel(df)
        self.name_view = QTableView()
        self.name_view.setModel(self.name_model)
        self.name_view.resize(800, 75)
        self.name_view.show()

    def search_universities_by_code(self):
        """ Search for university based on federal school code """

        # get user-inputted name and call procedure
        code = str(self.code_box.toPlainText())
        df = self.university_finder.search_universities_by_code(code)

        # view dataframe
        self.code_model = pandasModel(df)
        self.code_view = QTableView()
        self.code_view.setModel(self.code_model)
        self.code_view.resize(800, 75)
        self.code_view.show()

    def search_locations(self):
        """ Search all locations """

        # get dataframe
        df = self.university_finder.show_locations()

        # view dataframe
        self.loc_model = pandasModel(df)
        self.loc_view = QTableView()
        self.loc_view.setModel(self.loc_model)
        self.loc_view.resize(800, 500)
        self.loc_view.show()

        # change windows to search window
        self.view.close()
        self.locations = Locations(self.user, self.password,
                                   self.university_finder, self.loc_model, self.loc_view)
        self.locations.show()
        self.close()

    def search_reviews(self):
        """ Search all reviews """

        # get dataframe
        df = self.university_finder.show_reviews()

        # view dataframe
        self.rev_model = pandasModel(df)
        self.rev_view = QTableView()
        self.rev_view.setModel(self.rev_model)
        self.rev_view.resize(800, 500)
        self.rev_view.show()

        # change windows to search window
        self.view.close()
        self.reviews = Reviews(self.user, self.password,
                               self.university_finder, self.rev_model, self.rev_view)
        self.reviews.show()
        self.close()

    def view_clubs(self):
        """ View all clubs """

        # get df of results from query
        df = self.university_finder.view_clubs()

        # view dataframe
        self.clubs_model = pandasModel(df)
        self.clubs_view = QTableView()
        self.clubs_view.setModel(self.clubs_model)
        self.clubs_view.resize(500, 300)
        self.clubs_view.show()

    def view_alumni(self):
        """ View all notable alumni """

        # get df of results from query
        df = self.university_finder.view_notable_alumni()

        # view dataframe
        self.alumni_model = pandasModel(df)
        self.alumni_view = QTableView()
        self.alumni_view.setModel(self.alumni_model)
        self.alumni_view.resize(500, 300)
        self.alumni_view.show()

    def view_departments(self):
        """ View all departments """

        # get df of results from query
        df = self.university_finder.view_departments()

        # view dataframe
        self.deps_model = pandasModel(df)
        self.deps_view = QTableView()
        self.deps_view.setModel(self.deps_model)
        self.deps_view.resize(500, 300)
        self.deps_view.show()

    def go_back(self):
        """ Go to previous window """

        # close table view
        self.view.close()

        # open previous window obj
        self.search_or_watchlist = SearchorWatchlist(
            self.user, self.password, self.university_finder)
        self.search_or_watchlist.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class Filter(QMainWindow, FilterWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        FilterWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.filter_button.clicked.connect(self.filter)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def filter(self):
        """ Filter universities based on user-selected attributes """

        # get data from text boxes of each filter
        min_fee, max_fee = str(self.fee_box.toPlainText()), str(
            self.fee_box_2.toPlainText())

        min_tuition, max_tuition = str(self.tuition_box.toPlainText()), str(
            self.tuition_box_2.toPlainText())

        min_aid, max_aid = str(self.aid_box.toPlainText()), str(
            self.aid_box_2.toPlainText())

        min_sat, max_sat = str(self.sat_box.toPlainText()), str(
            self.sat_box_2.toPlainText())

        min_rank, max_rank = str(self.rank_box.toPlainText()), str(
            self.rank_box_2.toPlainText())

        min_body, max_body = str(self.body_box.toPlainText()), str(
            self.body_box_2.toPlainText())

        min_campus, max_campus = str(self.campus_box.toPlainText()), str(
            self.campus_box_2.toPlainText())

        min_acceptance, max_acceptance = str(self.acceptance_box.toPlainText()), str(
            self.acceptance_box_2.toPlainText())

        # make dataframe from filters
        df = self.university_finder.search_universities(min_fee, max_fee, min_tuition, max_tuition, min_aid, max_aid, min_sat, max_sat, min_rank, max_rank,
                                                        min_body, max_body, min_campus, max_campus, min_acceptance, max_acceptance)

        # close table view
        self.view.close()

        # view dataframe
        self.filtered_model = pandasModel(df)
        self.filtered_view = QTableView()
        self.filtered_view.setModel(self.filtered_model)
        self.filtered_view.resize(800, 500)
        self.filtered_view.show()

        # change windows to add_to_watchlist window
        self.add_to_watchlist = AddtoWatchlist(
            self.user, self.password, self.university_finder, self.model, self.filtered_view)
        self.add_to_watchlist.show()
        self.university_finder.shutdown()
        self.close()

    def go_back(self):
        """ Go to previous window """

        # close table view
        self.view.close()
        self.filtered_view.close()

        # open previous window obj
        self.search = Search(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.filtered_view.close()
        self.close()


class AddtoWatchlist(QMainWindow, AddWatchlistWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        AddWatchlistWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = UniversityFinder()
        self.university_finder.authenticate(user, password)

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.add_uni_button.clicked.connect(self.add_to_watchlist)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def add_to_watchlist(self):
        """ Add university to watchlist """

        name = str(self.name_box.toPlainText())
        notes = str(self.notes_box.toPlainText())
        self.university_finder.add_to_watchlist(name, notes)

        # close view and open new view of watchlist
        self.view.close()

        df = self.university_finder.show_watchlist()
        self.watchlist_model = pandasModel(df)
        self.watchlist_view = QTableView()
        self.watchlist_view.setModel(self.watchlist_model)
        self.watchlist_view.resize(800, 500)
        self.watchlist_view.show()

    def go_back(self):
        """ Go to previous window """

        # close table view
        self.view.close()

        # open previous window obj
        self.search = Search(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class Locations(QMainWindow, LocationsWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        LocationsWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.search_button.clicked.connect(self.search_locations)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def search_locations(self):
        """ Search locations """

        # get dataframe
        city = str(self.city_box.toPlainText())
        state = str(self.state_box.toPlainText())

        if city and state:
            df = self.university_finder.search_locations(city, state)
        elif not city:
            df = self.university_finder.search_locations_by_state(state)
        elif not state:
            df = self.university_finder.search_locations_by_city(city)

        # close table view
        self.view.close()

        # view dataframe
        self.filtered_model = pandasModel(df)
        self.filtered_view = QTableView()
        self.filtered_view.setModel(self.filtered_model)
        self.filtered_view.resize(500, 500)
        self.filtered_view.show()

        # change windows to add_to_watchlist window
        self.add_to_watchlist = AddtoWatchlist(
            self.user, self.password, self.university_finder, self.model, self.filtered_view)
        self.add_to_watchlist.show()
        self.university_finder.shutdown()
        self.close()

    def go_back(self):
        """ Go to previous window """

        # get df of results from query
        df = self.university_finder.show_universities()

        # view dataframe
        self.search_model = pandasModel(df)
        self.search_view = QTableView()
        self.search_view.setModel(self.search_model)
        self.search_view.resize(800, 500)
        self.search_view.show()

        # close table view
        self.view.close()

        # open previous window obj
        self.search = Search(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
        self.close()


class Reviews(QMainWindow, ReviewsWindow):

    def __init__(self, user, password, university_finder, pandasModel, tableView):
        QMainWindow.__init__(self)
        ReviewsWindow.__init__(self)
        self.setupUi(self)

        # initialize object to utilize database
        self.user, self.password = user, password
        self.university_finder = university_finder

        # initialize pandasModel and tableView
        self.model = pandasModel
        self.view = tableView

        # run functions
        self.search_button.clicked.connect(self.search_reviews)
        self.back_button.clicked.connect(self.go_back)
        self.shutdown_db_button.clicked.connect(self.exit_app)

    def search_reviews(self):
        """ Search reviews """

        # get dataframe
        rating = str(self.rating_box.value())
        df = self.university_finder.search_reviews(rating)

        # close table view
        self.view.close()

        # view dataframe
        self.filtered_model = pandasModel(df)
        self.filtered_view = QTableView()
        self.filtered_view.setModel(self.filtered_model)
        self.filtered_view.resize(500, 500)
        self.filtered_view.show()

        # change windows to add_to_watchlist window
        self.add_to_watchlist = AddtoWatchlist(
            self.user, self.password, self.university_finder, self.model, self.filtered_view)
        self.add_to_watchlist.show()
        self.university_finder.shutdown()
        self.close()

    def go_back(self):
        """ Go to previous window """

        # get df of results from query
        df = self.university_finder.show_universities()

        # view dataframe
        self.search_model = pandasModel(df)
        self.search_view = QTableView()
        self.search_view.setModel(self.search_model)
        self.search_view.resize(800, 500)
        self.search_view.show()

        # close table view
        self.view.close()

        # open previous window obj
        self.search = Search(self.user, self.password,
                             self.university_finder, self.model, self.view)
        self.search.show()
        self.close()

    def exit_app(self):
        """ Shutdown db and close application """

        self.university_finder.shutdown()
        self.view.close()
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
