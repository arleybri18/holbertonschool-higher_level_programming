#!/usr/bin/python3
""" This script return filter states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE
                name LIKE BINARY "N%" ORDER BY id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
