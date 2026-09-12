# This file will for now just host the health check so

# Get the server running

# Have a variable which determines the port number

# When hit return navidrome connector working

# import
import uvicorn
from fastapi import  FastAPI
import os

# defin the app and root with fastAPI
app = FastAPI()

CONNECTOR_PORT_NUMBER = 6769
CONNECTOR_API_PATH = "/connector"

# Get Tailscale domain
tailscale_domain = os.getenv("TAILSCALE_DOMAIN")
print(f"here is tailscale domain: {tailscale_domain}")

# Command to get tailscale IP address

@app.post("/")
async def read_root():
    return {"File Location: ": "Root"}
@app.post(CONNECTOR_API_PATH)
async def read_connector():
    return {"File Location: ":  CONNECTOR_API_PATH}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=CONNECTOR_PORT_NUMBER)
