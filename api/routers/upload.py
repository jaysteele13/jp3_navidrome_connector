 # Import fast API they offer a subrouting option for what I am trying ot do.
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

# Get class
from utils.classes import Song_Metadata


# Define router to allow this Structure to work!
router = APIRouter()

	
@router.get("/upload")
async def post_upload(song_metadata: Song_Metadata(), song_file: UploadFile, album_cover: Optional[UploadFile], artist_cover: Optional[UploadFile]):

	# Define the parameters, metadata should be defined like the pydantic class
	# Learn how we can add parameters to FastAPI
	
	return JSONResponse(
        content={"status": "Upload time like"},
        status_code=200
    )
	
	
