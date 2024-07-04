import sqlite3

fhand = open('Py4e Vocab V2.txt')

#process the file line for line
for line in fhand:
    words = line.split()
    defin = words[1]
    
