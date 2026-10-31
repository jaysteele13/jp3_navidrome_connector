 # Import fast API they offer a subrouting option for what I am trying ot do.
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.exc import DataError, IntegrityError, OperationalError, SQLAlchemyError

# import typing for optional
from typing import Optional, Annotated

# Get class
from utils.classes import Song_Metadata, Song, ErrorResponse

# Get Helper Class
from .helpers.validation import validate_song, validate_file, error_response



# inherit session to begin to make Database Calls!
from backend.db.db import SessionDep
from backend.db.db.db_helpers.insert import add_song



# Define router to allow this Structure to work!
router = APIRouter()


#  Song_Metadata, song_file: UploadFile, album_cover: Optional[UploadFile], artist_cover: Optional[UploadFile
@router.post("/upload")
async def post_upload(session: SessionDep, title: Annotated[str, Form()], artist:Annotated[str, Form()], album:Annotated[str, Form()] ,song_file: UploadFile,
year: Annotated[Optional[int], Form()] = None ,genre: Annotated[Optional[str], Form()]= None, album_cover: UploadFile | None = None,
artist_cover: UploadFile | None = None,):

	# Content type of pydantic model and upload file are completely different, so we cannot mix these due to http protocol not allowing the mix of
	# content-type
	
	# Rebuild Song Metadata
	song_metadata = Song_Metadata(title=title, artist=artist, album=album, year=year, genre=genre)
	song = Song(**song_metadata.model_dump(), file_path="")
	
	# Validate Song intially
	response = validate_song(song)
	
	# Return if Song Validation and Matching Fail
	if response.status_code != 200:
		return error_response(response)
		
	# Validate song file
	response = validate_file(song_file)
	if response.status_code != 200:
		return error_response(response)
	
	# add song into database
	response = add_song(song)
	if response.status_code != 200:
		return error_response(response)
	
	
	

	# Define the parameters, metadata should be defined like the pydantic class
	# Learn how we can add parameters to FastAPI
	session.refresh(song)
	return JSONResponse(
        content={"status": f"Song metadata. Title: {song_metadata.title}\nArtist: {song_metadata.artist}"
        f". Album {song_metadata.album}, \n/n Year and Genre: {song_metadata.year} and {song_metadata.genre}"},
        status_code=200
    )
	
	
