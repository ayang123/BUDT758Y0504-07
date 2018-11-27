from random import randint
import math
import time
import csv
import sqlite3


conn = sqlite3.connect('jobs.db')

c = conn.cursor()

res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print name[0]

res = c.execute("SELECT * FROM Organization")
for record in res:
    print record

#orgs = []
#
#count = 0
#with open('final_org.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    for row in csv_reader:
#        if count == 0:
#            count += 1
#        else:
#            orgs.append((row[0], sqlite3.Binary(row[1]), row[2]))
#
#c.executemany("INSERT INTO Organization VALUES (?, ?, ?)", orgs)

#res = c.execute("DELETE FROM Organization")

#conn.commit()

conn.close()


#with open('final_org.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    for row in csv_reader:
#        aDict[row[1]] = row[0]
