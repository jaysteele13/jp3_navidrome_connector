# Import fast API they offer a subrouting option for what I am trying ot do.
from fastapi import APIRouter
from fastapi.responses import JSONResponse


# Define router to allow this Structure to work!
router = APIRouter()

	
@router.get("/health")
async def read_health_check():
	# Check the current system if Port is running. Only return 200 for now, if port is not
	# open we will get a seperate error.
	
	# If there are other errors in other endpoints and this is 200
	# inspect other logs - would splunk be good for this?
	
	# CONNECTOR_PORT_NUMBER = 6769 # will change to find the real port soon.
	# For future we could test
	# the time it takes to respond?
	
	# Run lsof command to check if this port is being ran!
	return JSONResponse(
        content={"status": "Looking Swell Chap!"},
        status_code=200
    )
	
	
