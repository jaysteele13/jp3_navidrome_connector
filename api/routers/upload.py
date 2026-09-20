 # Import fast API they offer a subrouting option for what I am trying ot do.
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse

# import typing for optional
from typing import Optional, Annotated

# Get class
from utils.classes import Song_Metadata


# Define router to allow this Structure to work!
router = APIRouter()

#  Song_Metadata, song_file: UploadFile, album_cover: Optional[UploadFile], artist_cover: Optional[UploadFile
@router.post("/upload")
async def post_upload(title: Annotated[str, Form()], artist:Annotated[str, Form()], album:Annotated[str, Form()] ,song_file: UploadFile,
year: Annotated[Optional[int], Form()] = None ,genre: Annotated[Optional[str], Form()]= None, album_cover: UploadFile | None = None,
artist_cover: UploadFile | None = None):

	# Content type of pydantic model and upload file are completely different, so we cannot mix these due to http protocol not allowing the mix of
	# content-type
	
	# Rebuild Song Metadata
	song_metadata = Song_Metadata(title=title, artist=artist, album=album, year=year, genre=genre)
	

	# Define the parameters, metadata should be defined like the pydantic class
	# Learn how we can add parameters to FastAPI
	
	return JSONResponse(
        content={"status": f"Song metadata. Title: {song_metadata.title}\nArtist: {song_metadata.artist}"
        f". Album {song_metadata.album}, \n/n Year and Genre: {song_metadata.year} and {song_metadata.genre}"},
        status_code=200
    )
	
	
