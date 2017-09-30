# !/usr/bin/python3.5
import pymysql
db = pymysql.connect("localhost", "root", "password", "movie")
cursor = db.cursor()

try:
    def desc(table):
        sql = "desc " + table
        print("+-----------+-------------+------+-----+---------+-------+")
        print("| Field     | Type        | Null | Key | Default | Extra |")
        print("+-----------+-------------+------+-----+---------+-------+")
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("| "+str(row[0]).ljust(10)+"| "+str(row[1]).ljust(12)+"| "+str(row[2]).ljust(5)+"| "+str(row[3]).ljust(4)+"| "+str(row[4]).ljust(8)+"| "+str(row[5]).ljust(6)+"|")
            print("+-----------+-------------+------+-----+---------+-------+")

except:
    print("Error: unable to fetch data")

