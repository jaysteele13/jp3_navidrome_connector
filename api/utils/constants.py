from utils.classes import ErrorResponse

CONNECTOR_PORT_NUMBER = 6769
CONNECTOR_API_PATH = "/connector"

# Absolute Path
ROOT = "/home/jay"

DB_PATH = f"sqlite:///{ROOT}/Documents/databases/db.db"

# Status Codes
DUPLICATE_ENTRY_RESP = ErrorResponse(reason="", status_code=409)
INVALID_VALUES_RESP = ErrorResponse(reason="", status_code=422)
DATABASE_UNAVAILABLE_RESP = ErrorResponse(reason="", status_code=503)
GENERIC_DB_ERROR = ErrorResponse(reason="", status_code=500)
