#!/usr/bin/python3
"""
<<<<<<< HEAD
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
=======
4-cities_by_state module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
