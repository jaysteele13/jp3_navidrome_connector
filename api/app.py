# import
import uvicorn
from fastapi import  FastAPI
import os

# import the routers
from routers import health, upload

# import constants
from utils.constants import *

from backend.db.db import Database

# define the app and root with fastAPI
app = FastAPI()

# Initialise all Routes
app.include_router(health.router)
app.include_router(upload.router)


# Initialise the Session Dependency for whole app
db = Database()
engine = db.engine

def get_session():
    with Session(engine) as session:
        yield session


# Have SessionDep at the top
SessionDep = Annotated[Session, Depends(get_session)]



@app.post("/")
async def read_root():
    return {"File Location: ": "Where in PI this is all saved"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=CONNECTOR_PORT_NUMBER)
