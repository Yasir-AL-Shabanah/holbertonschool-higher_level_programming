#!/usr/bin/python3
"""List states starting with 'N' from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
