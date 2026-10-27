import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

# Bring in helper
from .db_helpers.connect import connect_to_db
from .db_helpers.insert import insert_song

import asyncio # for testing
from utils.classes import Song_Metadata

from typing import Annotated
from sqlmodel import Session

from fastapi import Depends


# We will use SQL acadmy as they manage memory better for dependency injection
class Database:
	def __init__(self, db_path=DB_PATH):
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
	



# Initialise the Session Dependency for whole app
db = Database()
engine = db.engine

def get_session():
    with Session(engine) as session:
        yield session


# Have SessionDep at the top - DI
SessionDep = Annotated[Session, Depends(get_session)]	 
