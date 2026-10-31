
from sqlmodel import SQLModel, Field 
from uuid import uuid4, UUID

class Song_Metadata(SQLModel):
	title: str 
	artist: str
	album: str
	year: int | None
	genre: str | None


# Create Song Table # should be Songs delete in SQL and try again  
class Song(Song_Metadata, table=True):
	# Additional; Fields
	id: UUID = Field(default_factory=uuid4, primary_key=True)
	
	file_path: str # required
	album_path: str | None = None # can be optional files so therefore be empty
	artist_path: str | None = None # can be optional files
	
	# Must make index / unqiue key for Song_metadta.title, aritst and album combined (unique identity)
	# Revist indexes later! Index(Song_Metadata.title, Song_Metadta.artist, Song_Metadata.album)






