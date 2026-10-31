
from sqlmodel import SQLModel, Field 
from sqlalchemy import UniqueConstraint
from uuid import uuid4, UUID

class Song_Metadata(SQLModel):
	title: str = Field(index=True)
	artist: str = Field(index=True)
	album: str = Field(index=True)
	year: int | None
	genre: str | None
	
	__table_args__ = (
		UniqueConstraint("title", "artist", "album", name="uq_song_artist_album"),
	)


# Create Song Table # should be Songs delete in SQL and try again  
class Song(Song_Metadata, table=True):
	# Additional; Fields
	id: UUID = Field(default_factory=uuid4, primary_key=True)
	
	file_path: str # required
	album_path: str | None = None # can be optional files so therefore be empty
	artist_path: str | None = None # can be optional files
	
	# Must make index / unqiue key for Song_metadta.title, aritst and album combined (unique identity)
	# Revist indexes later! Index(Song_Metadata.title, Song_Metadta.artist, Song_Metadata.album)






