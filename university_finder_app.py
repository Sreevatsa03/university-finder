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

    def search_universities_by_application_fee(self, min_val, max_val):
        """ Search university by application fee """

        query = """
            call search_by_application_fee(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_early_application(self, val):
        """ Search university by early application """

        query = """
            call search_by_has_early_application(%s);
            """

        return self.db.callProc(query, [val])

    def search_universities_by_tuition(self, min_val, max_val):
        """ Search university by tuition """

        query = """
            call search_by_tuition(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_aid(self, min_val, max_val):
        """ Search university by aid """

        query = """
            call search_by_avg_aid_awarded(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_SAT(self, min_val, max_val):
        """ Search university by avg SAT """

        query = """
            call search_by_avg_SAT(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_ranking(self, min_val, max_val):
        """ Search university by ranking """

        query = """
            call search_by_ranking(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_student_body_size(self, min_val, max_val):
        """ Search university by student body size """

        query = """
            call search_by_student_body_size(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_campus_size(self, min_val, max_val):
        """ Search university by camous size """

        query = """
            call search_by_campus_size(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_public(self, val):
        """ Search university by public """

        query = """
            call search_by_is_public(%s);
            """

        return self.db.callProc(query, [val])

    def search_universities_by_acceptance(self, min_val, max_val):
        """ Search university by acceptance rate """

        query = """
            call search_by_acceptance_rate(%s, %s);
            """

        return self.db.callProc(query, [min_val, max_val])

    def search_universities_by_state(self, val):
        """ Search university by state """

        query = """
            call search_by_state(%s);
            """

        return self.db.callProc(query, [val])

    def search_universities_by_city(self, val):
        """ Search university by city """

        query = """
            call search_by_city(%s);
            """

        return self.db.callProc(query, [val])

    def add_to_watchlist(self, name, notes):
        """ Add university to watchlist """

        query = """
            call add_to_watchlist(%s, %s);
            """

        return self.db.callProc(query, [name, notes])

    def show_watchlist(self):
        """ Display all universities in watchlist """

        query = f"""
            select *
            from watchlisted_university;
            """

        return self.db.execute(query)


# def main():
#     finder = UniversityFinder()
#     finder.authenticate('root', 'MySQLSnukala03#')


#     finder.add_to_watchlist('Columbia University', 'cool')
#     print(finder.show_watchlist())

# if __name__ == '__main__':
#     main()