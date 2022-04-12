#!/usr/bin/env python
# -*- coding: utf-8 -*-


# %% Simple selector (MySQL database)
# import pymysql for a simple interface to a MySQL DB

import pymysql

def 

def main():
    username = input("Please enter your username for the MySQL connection.\n")
    password = input("Please enter your password for the MySQL connection.\n")

    try:
        cnx = pymysql.connect(host='localhost', user=username, password=password,
                              db='sharkdb', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    except pymysql.err.OperationalError as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

    finally:
        cnx.close()


if __name__ == '__main__':
    main()
