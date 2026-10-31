from sqlmodel import SQLModel

class Song_Response(SQLModel):
	meta: Song_Metadata
	file_path: str
	album_path: str | None = None
	album_path: str | None = None
	
	
	
class Song_Update(SQLModel):
	 title: str | None = None
	 artist: str | None = None
	 album: str | None = None
	 year: int | None = None
	 genre: str | None = None
