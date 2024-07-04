import sqlite3

#read file and parse data
filename = ('Py4e Vocab V2.txt')
terms_definitions = []

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if '|' in line:
            term, definition = line.split('|', 1)
            term = term.strip()
            definition = definition.strip()
            terms_definitions.append((term, definition))

#connect to a SQL database or create one
conn = sqlite3.connect('PY4Evocab.db')

#create cursor object
cursor = conn.cursor()

#create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS glossary (
    term TEXT PRIMARY KEY,
    definition TEXT NOT NULL
);
'''
