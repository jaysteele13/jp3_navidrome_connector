from utils.classes import ErrorResponse, Song
from fastapi.responses import JSONResponse
from fastapi import UploadFile
# inherit session to begin to make Database Calls!
from backend.db.db import SessionDep

def error_response(error: ErrorResponse) -> JSONResponse:
	return JSONResponse(status_code=error.status_code, content=error.model_dump())
	
	
	
def validate_song(song: Song, session: SessionDep) -> ErrorResponse:
	# Should return something like  class
	
	print("Validate Song (Blank for Now) Check in Read and ensure this song does not alreayd exist")
	
	return ErrorResponse(status_code=200, reason="Song Successfully Validated!")

def validate_file(song_file: UploadFile, session: SessionDep) -> ErrorResponse:
	# Should return something like  class
	
	print("Validate File (Blank for Now) Ensure this is within allowed file types of ID3 Tagging")
	
	return ErrorResponse(status_code=200, reason="Song File Validated!")
