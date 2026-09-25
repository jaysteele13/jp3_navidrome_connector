import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

def connect_to_db():
	try:
		
		conn = sqlite3.connect(DB_PATH)  # Creates a new database file if it doesn’t exist
		cursor = conn.cursor()
		
		# we cretae indexes later in this flow!
		# Instantiate Tables if they do not exist
		song_table_creation = f"""
		CREATE TABLE IF NOT EXISTS {DB_SONGS_TABLE}(
		id TEXT PRIMARY KEY,
		song_title TEXT NOT NULL,
		album TEXT NOT NULL,
		artist TEXT NOT NULL,		
		genre TEXT,
		year TEXT,
		album_path TEXT,
		artist_path TEXT,
		UNIQUE (song_title, album, artist)
		)
		"""
		
		# Create Index to avoid duplicates

		cursor.execute(song_table_creation)
		return conn, cursor # Perhaps use yield and contextlib though I do not know enough about this.
	except Exception as e:
		print(f"Error in database instantiation, error: {e}")

