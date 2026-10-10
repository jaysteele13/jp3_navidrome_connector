import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

# Bring in helper
from .db_helpers.connect import connect_to_db
from .db_helpers.insert import insert_song

import asyncio # for testing
from utils.classes import Song_Metadata


# We will use SQL acadmy as they manage memory better for dependency injection
class Database:
	async def __init__(self, db_path=DB_PATH):
		self.engine = connect_to_db()
		
	
	# Generic Query of DB
	async def query(self, query, params=None):
		self.cursor.execute(query, params or ())
		return self.cursor.fetchall()
		
	async def insert_song(self, song_metadata: Song_Metadata, album_cover = "", artist_cover = ""):
		insert_song(self.conn, self.cursor, song_metadata, album_cover, artist_cover)
	
	async def save(self):
		self.cursor.commit()
	
	async def close(self):
		self.conn.close()
	



# database_instance = Database()

# DI funciton
async def get_db():
	try:
		print(f"databse type:  {type(database_instance)}")
		yield database_instance
	finally:
		print("Closing database after failing to grab db instance!")
		await database_instance.close()
		

async def main():
		
	# DB instance
	database_instance = Database() # test with this class first. Next time, change songs to match 
	# await get_db() # is an async generator as FastAPI handles these for DI
	
	# Add DB CRUD - just do create for now then we will focus on other CRUD later!
	# Begin to add DB logic to upload (basic query and adding basic data)
	# We will then focus on id3
	# Then how we will move the file!
	
	# To delete tables go in terminal:
	# sqlite3
	# .table to show tables then
	# drop table table_name

	# db testing
	#db insert song
	# test data
	song_metadata = Song_Metadata(title="Thank you for the music", album="Mamma Mia", artist = "ABBA", year=1977, genre="Disco")
	
	await database_instance.insert_song(song_metadata)


	# Query db to see if it works
	query = f"SELECT * FROM {DB_SONGS_TABLE}"
	res =  await database_instance.query(query)
	print(f"Query DB: {res}")

	# close this when finished.
	await database_instance.close()
# test db
if __name__ == "__main__":
	asyncio.run(main())
