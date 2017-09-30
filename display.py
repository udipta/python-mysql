# !/usr/bin/python3.5
import pymysql
db = pymysql.connect("localhost", "root", "password", "movie")
cursor = db.cursor()


def disp(table):

        sql = "select * from " + table

        if table == 'actor':
            actor(sql)
        elif table == 'director':
            director(sql)
        elif table == 'movies':
            movies(sql)
        elif table == 'movie_cast':
            cast(sql)
        elif table == 'rating':
            rating(sql)
        else:
            print("Invalid Entry")


try:
    def actor(sql):

        cursor.execute(sql)
        print("\n-----------------------------------")
        print("| ACT_ID |    ACT_NAME     | SEX |")
        print("-----------------------------------")

        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            sex = row[2]
            print("|   " + str(id).ljust(5) + "| " + str(name).ljust(15) + " |  " + str(sex).ljust(3) + "|")
            print("-----------------------------------")


    def director(sql):

        cursor.execute(sql)
        print("\n--------------------------------------------")
        print("| DIR_ID |      DIR_NAME       | DIR_PHONE |")
        print("--------------------------------------------")

        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            phone = row[2]
            print("|   " + str(id).ljust(5) + "| " + str(name).ljust(20) + "| " + str(phone).ljust(10) + "|")
            print("--------------------------------------------")


    def movies(sql):

        cursor.execute(sql)
        print("\n----------------------------------------------------------------")
        print("| MOV_ID  |     MOV_TITLE       | MOV_YEAR | MOV_LANG | DIR_ID |")
        print("----------------------------------------------------------------")

        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            year = row[2]
            lang = row[3]
            d_id = row[4]
            print("|    " + str(id).ljust(5) + "| " + str(name).ljust(20) + "|   " + str(year).ljust(7) + "| " + str(
                lang).ljust(9) + "|   " + str(d_id).ljust(5) + "|")
            print("----------------------------------------------------------------")


    def cast(sql):

        cursor.execute(sql)
        print("\n-----------------------------")
        print("| ACT_ID | MOV_ID |  ROLE   |")
        print("-----------------------------")

        results = cursor.fetchall()
        for row in results:
            a_id = row[0]
            m_id = row[1]
            role = row[2]
            print("|   " + str(a_id).ljust(5) + "|  " + str(m_id).ljust(5) + " | " + str(role).ljust(8) + "|")
            print("-----------------------------")


    def rating(sql):

        cursor.execute(sql)
        print("\n------------------")
        print("| MOV_ID | STARS |")
        print("------------------")

        results = cursor.fetchall()
        for row in results:
            m_id = row[0]
            star = row[1]
            print("|  " + str(m_id).ljust(5) + " |  " + str(star).ljust(5) + "|")
            print("------------------")


except:
    print("Error: unable to fetch data")

