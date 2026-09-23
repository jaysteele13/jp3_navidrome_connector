import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

# Bring in helper
from .db_helpers.connect import connect_to_db
from .db_helpers.insert import insert_test

conn, cursor =  connect_to_db()

# Insert into test
insert_test(conn, cursor, 'test_5', 'another description')

# Query db to see if it works	
res = cursor.execute(f"SELECT * FROM {DB_SONGS_TABLE}")
print(f"Query DB: {res.fetchall()}")

# close this when finished.
conn.close() # close this bitch

# If I open a database, I must close it when I am done. I will need an execption that if api fails or is shutdown - always close the database!
	
