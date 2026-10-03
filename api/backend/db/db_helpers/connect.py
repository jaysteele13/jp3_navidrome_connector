import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE
from utils.classes import Song_Metadata


# Instantiate Database Path from given path form constants

# Create Song Table
class Song(Song_Metadata, table=True):
	# Additional; Fields
	id: UUID = Field(default_factory=uuid4, primary_key=True)
	
	file_path: str # required
	album_path: str | None = None # can be optional files so therefore be empty
	artist_path: str | None = None # can be optional files
	
	# Must make index / unqiue key for Song_metadta.title, aritst and album combined (unique identity)




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

