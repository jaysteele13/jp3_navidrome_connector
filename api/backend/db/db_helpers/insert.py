import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

def insert_test(conn, cursor, id1, des):
	
	# Instantiate Tables if they do not exist
	test_table_insertion = f"""
	INSERT INTO {DB_SONGS_TABLE} VALUES (?, ?)
	"""

	# Fix insert and clean up practice later
	try:
		cursor.execute(test_table_insertion, (id1, des))
		print(f"added: id: {id1} and des: {des}") # Add try catch!
		
		# Save this change!
		conn.commit()
	except Exception as e:
		print(f"Error trying to insert table data: {e}")
		
