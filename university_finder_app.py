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

        try:
            query = f"""
                select *
                from university
                order by ranking;
                """

            return self.db.execute(query)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_name(self, name):
        """ Search university by name """

        try:
            query = """
                call search_by_name(%s);
                """

            return self.db.callProc(query, [name])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_code(self, code):
        """ Search university by federal school code """

        try:
            query = """
                call search_by_federal_school_code(%s);
                """

            return self.db.callProc(query, [code])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def view_clubs(self):
        """ View all clubs """

        try: 
            query = f"""
                select c.name as club_name, c.type, u.name as university_name 
                from club as c
                join university as u
                on c.university = u.federal_school_code
                order by university_name;
                """

            return self.db.execute(query)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def view_notable_alumni(self):
        """ View all notable alumni """

        try:
            query = f"""
                select n.first_name, n.last_name, n.occupation, n.est_net_worth, n.graduating_class, u.name as university_name from notable_alum as n
                join university as u
                on n.university = u.federal_school_code
                order by university_name;
                """

            return self.db.execute(query)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def view_departments(self):
        """ View all departments """

        try:
            query = f"""
                select d.name, d.num_students, u.name as university_name from department as d
                join university as u
                on d.university = u.federal_school_code
                order by university_name;
                """

            return self.db.execute(query)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_application_fee(self, min_val, max_val):
        """ Search university by application fee """

        try:
            query = """
                call search_by_application_fee(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_early_application(self, val):
        """ Search university by early application """

        try:
            query = """
                call search_by_has_early_application(%s);
                """

            return self.db.callProc(query, [val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_tuition(self, min_val, max_val):
        """ Search university by tuition """

        try:
            query = """
                call search_by_tuition(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_aid(self, min_val, max_val):
        """ Search university by aid """

        try:
            query = """
                call search_by_avg_aid_awarded(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_SAT(self, min_val, max_val):
        """ Search university by avg SAT """

        try:
            query = """
                call search_by_avg_SAT(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_ranking(self, min_val, max_val):
        """ Search university by ranking """

        try:
            query = """
                call search_by_ranking(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_student_body_size(self, min_val, max_val):
        """ Search university by student body size """
        
        try:
            query = """
                call search_by_student_body_size(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_campus_size(self, min_val, max_val):
        """ Search university by camous size """

        try:
            query = """
                call search_by_campus_size(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_public(self, val):
        """ Search university by public """

        try:
            query = """
                call search_by_is_public(%s);
                """

            return self.db.callProc(query, [val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_acceptance(self, min_val, max_val):
        """ Search university by acceptance rate """
        try:
            query = """
                call search_by_acceptance_rate(%s, %s);
                """

            return self.db.callProc(query, [min_val, max_val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_state(self, val):
        """ Search university by state """

        try:
            query = """
                call search_by_state(%s);
                """

            return self.db.callProc(query, [val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities_by_city(self, val):
        """ Search university by city """
        
        try:
            query = """
                call search_by_city(%s);
                """

            return self.db.callProc(query, [val])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_universities(self, fee_min, fee_max, tuition_min, tuition_max, aid_min, aid_max, sat_min, sat_max, rank_min, rank_max,
                            body_min, body_max, campus_min, campus_max, acceptance_min, acceptance_max):
        """ Search university by all fields """

        try:
            query = """
                call search_universities(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """

            return self.db.callProc(query, [fee_min, fee_max, tuition_min, tuition_max, aid_min, aid_max, sat_min, sat_max, rank_min, rank_max,
                                            body_min, body_max, campus_min, campus_max, acceptance_min, acceptance_max])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def add_to_watchlist(self, name, notes):
        """ Add university to watchlist """

        try:
            query = """
                call add_to_watchlist(%s, %s);
                """

            return self.db.callProc(query, [name, notes])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def show_watchlist(self):
        """ Display all universities in watchlist """

        try:
            query = f"""
                select *
                from watchlisted_university;
                """

            return self.db.execute(query)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def show_locations(self):
        """ Display all locations """

        try:
            query = f"""
                select l.state, l.city, l.population, l.political_standing, l.climate_description, l.university, u.name from location as l
                join university as u
                on l.university = u.federal_school_code
                order by university;
                """

            return self.db.execute(query)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_locations_by_city(self, city):
        """ Search location by city """

        try:
            query = """
                call search_location_by_city(%s);
                """

            return self.db.callProc(query, [city])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_locations_by_state(self, state):
        """ Search location by state """

        try:
            query = """
                call search_location_by_state(%s);
                """

            return self.db.callProc(query, [state])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_locations(self, city, state):
        """ Search location by city and state """

        try:
            query = """
                call search_location(%s, %s);
                """

            return self.db.callProc(query, [city, state])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def show_reviews(self):
        """ Display all reviews """

        try:
            query = f"""
                select r.star_rating, r.description, r.author, r.university, u.name from review as r
                join university as u
                on r.university = u.federal_school_code
                order by university;
                """

            return self.db.execute(query)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def search_reviews(self, star_rating):
        """ Search location by city and state """

        try:
            query = """
                call filter_reviews(%s);
                """

            return self.db.callProc(query, [star_rating])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def write_review(self, star_rating, description, author, university):
        """ Search location by city and state """

        try:
            query = """
                call write_review(%s, %s, %s, %s);
                """

            return self.db.callProc(query, [star_rating, description, author, university])

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def show_watchlist(self):
        """ Display all universites in watchlist """

        try:
            query = f"""
                select *
                from watchlisted_university
                order by ranking;
                """

            return self.db.execute(query)
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def edit_notes(self, university, notes):
        """ Update notes of a watchlisted university """

        try:
            query = """
                call update_notes(%s, %s);
                """

            return self.db.callProc(query, [university, notes])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    def remove_from_watchlist(self, university):
        """ Remove a watchlisted university """

        try:
            query = """
                call remove_from_watchlist(%s);
                """

            return self.db.callProc(query, [university])
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
