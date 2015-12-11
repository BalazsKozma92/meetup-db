import re
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="",charset='utf8',use_unicode=True, autocommit=True)
cursor = db.cursor()

sql_create = ("Users\Kozma Balazs\PycharmProjects\sql\create.sql")
sql_insert = ("Users\Kozma Balazs\PycharmProjects\sql\insert.sql")

print("Welcome the simple meetup SQL system!\n","*"*37,"\n", \
      "1 # Create the database\n" \
      " 2 # Insert datas\n" \
      " 3 # DQL scripts\n" \
      " 4 # Drop database\n")
menu = input("Choose a menu: ")

if menu == "1":
    print("\n[INFO] Executing SQL script file: '%s'" % (sql_create))
    statement = ""
    for line in open(sql_create):
        if re.match(r'--', line):
            continue
        if not re.search(r'[^-;]+;', line):
            statement += line.replace("\n", "").replace("\t", "").replace("  ", " ")
        else:
            statement += line.replace("\n", "").replace("\t", "").replace("  ", " ")
            try:
                cursor.execute(statement)
            except:
                print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'")
            statement = ""
    print("[INFO] Executing successfully finished: '%s'" % (sql_create))
elif menu == "2":
    print("\n[INFO] Executing SQL script file: '%s'" % (sql_insert))
    statement = ""
    for line in open(sql_insert):
        if re.match(r'--', line):
            continue
        if not re.search(r'[^-;]+;', line):
            statement += line.replace("\n", "").replace("\t", "").replace("\\", "")
        else:
            statement += line.replace("\n", "").replace("\t", "").replace('\\', '')
            try:
                cursor.execute(statement)
            except:
                print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'")
            statement = ""
    print("[INFO] Executing successfully finished: '%s'" % (sql_insert))
elif menu == "3":
    print("1 # List all User\n" \
          "2 # List all meetups\n" \
          "3 # List meetups which are after 2015.11.27\n" \
          "4 # List that users who have introduction (NOT NULL)\n")
    almenu = input("Choose a script: ")
    if almenu == "1":
        query_allusers = "SELECT * FROM meetups_db.Users"
        cursor.execute(query_allusers)
        allusers = cursor.fetchall()
        for r in allusers:
            print(r[0], "", r[1], "", r[2], "", r[3], "", r[4], r[5])
    elif almenu == "2":
        query_meetups = "SELECT * FROM meetups_db.Meetups"
        cursor.execute(query_meetups)
        meetups = cursor.fetchall()
        for r in meetups:
            print(r[0], "", r[1], "", r[2], "", r[3], "", r[4])

    elif almenu == "3":
        query_meetups_after = "SELECT * FROM meetups_db.Meetups WHERE Start>'2015-11-27'"
        cursor.execute(query_meetups_after)
        meetups_after = cursor.fetchall()
        for r in meetups_after:
            print(r[0], "", r[1], "", r[2], "", r[3], "", r[4])

    elif almenu == "4":
        query_userNoIntro = "SELECT * FROM meetups_db.Users WHERE Introduction IS NOT NULL"
        cursor.execute(query_userNoIntro)
        userNoIntro = cursor.fetchall()
        for r in userNoIntro:
            print(r[0], "", r[1], "", r[2], "", r[3], "", r[4], r[5])

elif menu == "4":
    try:
        query_dropDatabase = "DROP DATABASE meetups_db"
        cursor.execute(query_dropDatabase)
        print("[INFO] Database dropped: 'meetups_db'")
    except:
        print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'")
else:
    print("Please enter a valid menu number.")