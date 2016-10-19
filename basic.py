import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

def average( tup ):
    sum = 0;
    for t in tup:
        sum += t[0]

    return sum / len(tup)


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

sum = 0


q = """
SELECT id 
FROM students
"""
c.execute(q)

idList = c.fetchall() 

print "name | id | average"

for id in idList:
    q = """
    SELECT mark 
    FROM courses
    WHERE id = %d
    """ % (id[0])
    c.execute(q)
    marks = c.fetchall()

    q = """
    SELECT name 
    FROM students
    WHERE id = %d
    """ % (id[0])
    c.execute(q)
    name = c.fetchall()[0][0]
    print "%s | %d | %d" %(name, id[0], average( marks ))
    
    #what do we do w it now



