import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

sum = 0


q = """
SELECT courses.mark 
FROM courses
WHERE id = 1
"""
c.execute(q)


l = c.fetchall() 
print l[1] + 1
