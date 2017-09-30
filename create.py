# !/usr/bin/python3.5
import pymysql
db = pymysql.connect("localhost", "root", "123", "movie")
cursor = db.cursor()
cursor.execute("use movie")


def create_table():

    # Open a file
    fo = open("movie.sql", "r+")

    while True:
        line = fo.readline()

        if line == '\n':
            continue

        string = line[:-1]
        cursor.execute(string)
        db.commit()
        if line == "":
            break

    cursor.close()

    # Close opened file
    fo.close()

try:
    create_table()
except:
    print("\n")
