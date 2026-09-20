import sqlite3

# Import Path of db
from utils.constants import DB_PATH

def insert_test(cursor, id1, des):
	
	# Instantiate Tables if they do not exist
	test_table_insertion = """
	INSERT INTO test VALUES (?, ?)
	"""

	# Fix insert and clean up practice later!
	cursor.execute(test_table_insertion, [(id1, des)])
	print(f"added: id: {id1} and des: {des}") # Add try catch!
