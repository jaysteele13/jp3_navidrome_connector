from pydantic import BaseModel

class Song_Metadata(BaseModel):
	title: str 
	artist: str
	album: str
	year: int
	genre: str
	
	
