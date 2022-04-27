#!/usr/bin/env python
# -*- coding: utf-8 -*-


# %% Simple selector (MySQL database)
# import pymysql for a simple interface to a MySQL DB

import mysql.connector
from dbutils import DBUtils
import pandas as pd


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

    def search_universities_by_name(self, name):
        """ Search university by name """

        query = """
            call search_by_name(%s);
            """

        return self.db.callProc(query, [name])

    def search_universities_by_code(self, code):
        """ Search university by federal school code """

        query = """
            call search_by_federal_school_code(%s);
            """

        return self.db.callProc(query, [code])

    def view_clubs(self):
        """ View all clubs """

        query = f"""
            select c.name as club_name, c.type, u.name as university_name 
            from club as c
	        join university as u
		    on c.university = u.federal_school_code
            order by university_name;
            """

        return self.db.execute(query)

    def view_notable_alumni(self):
        """ View all notable alumni """

        query = f"""
            select n.first_name, n.last_name, n.occupation, n.est_net_worth, n.graduating_class, u.name as university_name from notable_alum as n
	        join university as u
		    on n.university = u.federal_school_code
	        order by university_name;
            """

        return self.db.execute(query)

    def view_departments(self):
        """ View all departments """

        query = f"""
            select d.name, d.num_students, u.name as university_name from department as d
	        join university as u
		    on d.university = u.federal_school_code
	        order by university_name;
            """

        return self.db.execute(query)

# def main():
#     finder = UniversityFinder()
#     finder.authenticate('root', 'MySQLSnukala03#')
#     finder.search_universities_by_code("002627")

# if __name__ == '__main__':
#     main()