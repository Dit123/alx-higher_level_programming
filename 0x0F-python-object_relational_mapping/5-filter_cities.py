#!/usr/bin/python3
"""
<<<<<<< HEAD
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
=======
5-filter_cities module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    new_list = list(row[0] for row in rows)
    print(", ".join(new_list))
    cur.close()
    db.close()
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
