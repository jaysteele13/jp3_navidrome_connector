
from sqlmodel import SQLModel 

class Song_Metadata(SQLModel):
	title: str 
	artist: str
	album: str
	year: int | None
	genre: str | None
	

