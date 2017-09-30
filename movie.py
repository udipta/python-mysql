# !/usr/bin/python3.5
from query import *
from desc import *

def func():
    def loop():
        global x
        try:
            print("\ndo u want to continue?(1/0): ")
            x = int(input())
            if x == 1:
                return x
            elif x == 0:
                func()
        except:
            print("Program Terminated")
            cursor.close()
            quit()

    print("Options....\n1. Description\n2. Display Table content\n3.Query")
    a = int(input("Enter your choice: "))

    if a == 1:
        print(" \n---: Table Descriptions :---\n  ")
        i = 1
        while i:
            table = input("Enter the table name: ").lower()
            desc(table)
            i = loop()

    elif a == 2:
            print("\n---: Table Content :---\n  ")
            i = 1
            while i:
                table = input("Enter the table name: ").lower()
                disp(table)
                i = loop()

    elif a == 3:
        print("\nSQL queries are....\n")

        print("1. List the titles of all movies directed by ‘Hitchcock’.\n")
        print("2. Find the movie names where one or more actors acted in two or more movies.\n")
        print("3. List all actors who acted in a movie before 2000 and also in a movie after 2015 (use JOIN "
              "operation).\n")
        print("4. Find the title of movies and number of stars for each movie that has at least one rating")
        print("    and find the highest number of stars that movie received. Sort the result by movie title.\n")
        print("5. Update rating of all movies directed by ‘Steven Spielberg’ to 5.\n")

        i = 1
        while i:
            opt = int(input("Enter the Query no. : "))
            query(opt)
            i = loop()

    else:
        quit()

try:
       func()
except:
       pass
