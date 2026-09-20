import sqlite3

# Import Path of db
from utils.constants import DB_PATH

# Bring in helper
from .db_helpers.connect import connect_to_db
from .db_helpers.insert import insert_test

conn, cursor =  connect_to_db()

# Insert into test
insert_test(cursor, 'test_4', 'another description')

# Query db to see if it works	
res = cursor.execute("SELECT * FROM test")
print(f"Query DB: {res.fetchall()}")
conn.commit() # Save database changes
conn.close() # close this bitch
	
