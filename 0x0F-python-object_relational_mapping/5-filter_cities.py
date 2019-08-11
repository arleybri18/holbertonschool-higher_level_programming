#!/usr/bin/python3
""" This script return cities and states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities c
                LEFT JOIN states s ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id""", (argv[4],))
    rows = cur.fetchall()
    cont = 0
    for row in rows:
        if cont < len(rows) - 1:
            print("{}".format(row[0]), end=", ")
            cont += 1
        else:
            print("{}".format(row[0]))
    cur.close()
    db.close()
