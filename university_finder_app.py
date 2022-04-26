#!/usr/bin/env python
# -*- coding: utf-8 -*-


# %% Simple selector (MySQL database)
# import pymysql for a simple interface to a MySQL DB

import pymysql
import sys
from PyQt6 import QtWidgets, uic
# from university_finder_ui import UniversityFinderUI
from dbutils import DBUtils


class UniversityFinder():

    def __init__(self):
        self.db = DBUtils()

    def authenticate(self, user, password, database="universities", host="localhost"):
        """ Authenticate credentials to access database """

        self.db.authenticate(user, password, database, host)

    def shutdown(self):
        """ Close connection to db """

        self.db.close()

    def show_universities(self):
        """ Display all universites in order of ranking """

        query = f"""
            select *
            from university
            order by ranking;
            """

        return self.db.execute(query)

# def main():
    # open user interface
    # app = QtWidgets.QApplication(sys.argv)
    # window = UniversityFinderUI()
    # window.show()

    # initialize object to utilize database
    # university_finder = UniversityFinder()
    # university_finder.authenticate("root", "MySQLSnukala03#")
    # university_finder.shutdown()

    # close system
    # sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
