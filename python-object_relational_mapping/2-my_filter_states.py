#!/usr/bin/python3
"""Filter states by name using a value provided by the user.

This script is intentionally vulnerable to SQL injection for the task.
"""

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
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
