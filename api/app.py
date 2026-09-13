# import
import uvicorn
from fastapi import  FastAPI
import os

# import the routers
from routers import health

# import constants
from utils.constants import *

# defin the app and root with fastAPI
app = FastAPI()

# Initialise all Routes
app.include_router(health.router)

@app.post("/")
async def read_root():
    return {"File Location: ": "Where in PI this is all saved"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=CONNECTOR_PORT_NUMBER)
