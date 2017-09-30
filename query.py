# !/usr/bin/python3.5
from  linecache import getline
from display import *

q1 = getline("query.txt", 2)
q2 = getline("query.txt", 4)
q3 = getline("query.txt", 6)
q4 = getline("query.txt", 8)
q5a = getline("query.txt", 10)
q5b = getline("query.txt", 12)


def query(x):
    if x == 1:          Q1()
    elif x == 2:        Q2()
    elif x == 3:        Q3()
    elif x == 4:        Q4()
    elif x == 5:        Q5()
    else:
        print("Invaild Entry")


try:
    def Q1():
        cursor.execute(q1)
        print("\n-----------------------")
        print("|     MOV_TITLE       |")
        print("-----------------------")

        results = cursor.fetchall()
        for row in results:
            print("| " + str(row[0]).ljust(20) + "|")
            print("-----------------------")


    def Q2():
        cursor.execute(q2)
        print("\n----------------------")
        print("|     MOV_TITLE       |")
        print("-----------------------")

        results = cursor.fetchall()
        for row in results:
            print("| " + str(row[0]).ljust(20) + "|")
            print("-----------------------")


    def Q3():
        cursor.execute(q3)
        print("\n-----------------------------------------------------")
        print("|    ACT_NAME      |     MOV_TITLE       | MOV_YEAR |")
        print("-----------------------------------------------------")

        results = cursor.fetchall()
        for row in results:
            print("| " + str(row[0]).ljust(15) + "| " + str(row[1]).ljust(20) + "| " + str(row[2]).ljust(9) + "|")
            print("--------------------------------------------------")


    def Q4():
        cursor.execute(q4)
        print("\n-----------------------------------")
        print("|     MOV_TITLE       | MAX(STARS) |")
        print("------------------------------------")

        results = cursor.fetchall()
        for row in results:
            print("| " + str(row[0]).ljust(20) + "|     " + str(row[1]).ljust(6) + " |")
            print("------------------------------------")


    def Q5():
        cursor.execute(q5a)
        db.commit()
        rating(q5b)

except:
    print("Error: unable to fetch data")
