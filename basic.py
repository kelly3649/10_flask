import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

sum = 0

c.execute("SELECT courses.mark FROM courses where id = 1")

l = c.fetchall() 
print l[1] + 1
