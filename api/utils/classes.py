from pydantic import BaseModel

class Song_Metadata(BaseModel):
	title: str 
	artist: str
	album: str
	year: int | None
	genre: str | None
	
	
