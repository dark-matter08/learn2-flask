import sqlite3

conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()

sql_query = """ CREATE TABLE book (
    id integer PPRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

cursor.execute(sql_query)
