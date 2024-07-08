import sqlite3

# Read file and parse data
filename = 'Py4e Vocab V2.txt'
terms_definitions = []

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if '|' in line:
            term, definition = line.split('|', 1)
            term = term.strip()
            definition = definition.strip()
            terms_definitions.append((term, definition))

# Connect to a SQL database or create one
conn = sqlite3.connect('PY4Evocab.db')

# Create cursor object
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS glossary (
    term TEXT PRIMARY KEY,
    definition TEXT NOT NULL
);
'''
cursor.execute(create_table_query)

# Insert data into table
insert_data_query = '''
INSERT INTO glossary (term, definition) VALUES (?, ?);
'''
cursor.executemany(insert_data_query, terms_definitions)

# Commit changes and close
conn.commit()
conn.close()
