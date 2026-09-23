import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

def connect_to_db():
	try:
		
		conn = sqlite3.connect(DB_PATH)  # Creates a new database file if it doesn’t exist
		cursor = conn.cursor()
	
		# Instantiate Tables if they do not exist
		song_table_creation = f"""
		CREATE TABLE IF NOT EXISTS {DB_SONGS_TABLE}(
		ID TEXT PRIMARY KEY,
		Description TEXT)
		"""

		cursor.execute(song_table_creation)
		return conn, cursor # Perhaps use yield and contextlib though I do not know enough about this.
	except Exception as e:
		print(f"Error in database instantiation, error: {e}")

