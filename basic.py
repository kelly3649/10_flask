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

e = "\033[32m"
clear = "\033[0m"
f = "\033[35m"
g = "\033[34m"

print "%sname%s | %sid%s | %saverage%s\n___________________" % (e, clear, f, clear, g, clear)

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
    print "%s%s%s | %s%d%s | %s%d%s" %(e, name, clear, f, id[0], clear, g, average( marks ), clear)
    
    #what do we do w it now



