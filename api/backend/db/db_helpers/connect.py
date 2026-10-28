import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE
from utils.classes import Song_Metadata

from sqlmodel import Session, SQLModel, create_engine, Field
from uuid import uuid4, UUID
# from sqlalchemy import Index


# Instantiate Database Path from given path form constants

# Create Song Table
class Song(Song_Metadata, table=True):
	# Additional; Fields
	id: UUID = Field(default_factory=uuid4, primary_key=True)
	
	file_path: str # required
	album_path: str | None = None # can be optional files so therefore be empty
	artist_path: str | None = None # can be optional files
	
	# Must make index / unqiue key for Song_metadta.title, aritst and album combined (unique identity)
	# Revist indexes later! Index(Song_Metadata.title, Song_Metadta.artist, Song_Metadata.album)


def connect_to_db():
	connect_args = {"check_same_thread": False}
	
	# if all ready created ignore
	engine = create_engine(DB_PATH, connect_args=connect_args)
	
	SQLModel.metadata.create_all(engine)
	
	return engine

