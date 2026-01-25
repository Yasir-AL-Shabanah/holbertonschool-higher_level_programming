#!/usr/bin/python3
"""Safely filter states by name using parameterized queries."""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = db.cursor()
    query = (
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY %s "
        "ORDER BY id ASC"
    )
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
