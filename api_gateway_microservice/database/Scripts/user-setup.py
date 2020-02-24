#Python Script To read pet SQL File and execute them in directed database
#Created 2/2/20

import psycopg2
import time

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        if command == "":
            print("X\n")
        elif command != "":
            print(command + ";\n")
            cur.execute(command)

conn = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='user_db',
    user='postgres',
    password='postgres',
)

conn.autocommit = True

cur = conn.cursor()

#Run Scripts for user DB
executeScriptsFromFile("SQLFiles/user_init.sql")
cur.execute("Select * from users")
x = cur.fetchall()
print(x)

cur.close()

conn.close()