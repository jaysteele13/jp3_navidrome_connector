import sqlite3
import uuid

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE
from utils.classes import Song_Metadata

def insert_song(conn, cursor, song_metadata: Song_Metadata, album_path = "", artist_path = ""):
	
	# Instantiate Tables if they do not exist
	# fields to insert: id (uuid), song_title, album, artist, genre, year, album_path, artist_path

	test_table_insertion = f"""
	INSERT INTO {DB_SONGS_TABLE} VALUES (?, ?, ?, ?, ?, ?, ?, ?)
	"""

	# Fix insert and clean up practice later
	try:
		# generate a UUID
		song_id = str(uuid.uuid4())
		print(f"type of song_id: {type(song_id)}")
		
		cursor.execute(test_table_insertion, (song_id, song_metadata.title, song_metadata.album,
		song_metadata.artist, song_metadata.genre, song_metadata.year, album_path, artist_path))
		
		# Save this change!
		conn.commit()
	except Exception as e:
		print(f"Error trying to insert table data: {e}")
		
