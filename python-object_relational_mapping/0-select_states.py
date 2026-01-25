#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa.

This script connects to a MySQL server running on localhost at port 3306,
using the credentials passed as command line arguments and the database
name. It then retrieves and prints all rows from the states table
ordered by id in ascending order.
"""

import MySQLdb
import sys


def list_states(user, password, database):
    """Connect to MySQL server and list all states in the states table.

    Args:
        user (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database to use.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
