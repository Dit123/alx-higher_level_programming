#!/usr/bin/python3
"""
<<<<<<< HEAD
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
=======
1-filter_states module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
