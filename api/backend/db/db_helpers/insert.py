from backend.db.db import SessionDep
from utils.classes import Song, ErrorResponse
from sqlalchemy.exc import DataError, IntegrityError, OperationalError, SQLAlchemyError


# Import Database Failure Codes:
from utils.constants import DUPLICATE_ENTRY_RESP, GENERIC_DB_ERROR, INVALID_VALUES_RESP, DATABASE_UNAVAILABLE_RESP

def add_song(song: Song, session: SessionDep) -> ErrorResponse:
	try:
		session.add(song)
		session.commit()
		# If compiles here then SUCCESS
		return ErrorResponse(reason=f"Song: {song.title} officially added to db.", status_code=200)
		
	except IntegrityError:
		session.rollback()
		# Have Standardised Error Codes
		return ErrorResponse(DUPLICATE_ENTRY_RESP)
	except DataError:
		session.rollback()
		return ErrorResponse(INVALID_VALUES_RESP)
		
	except OperationalError:
		session.rollback()
		return ErrorResponse(DATABASE_UNAVAILABLE_RESP)
	except SQLAlchemyError:
		session.rollback()
		return ErrorResponse(GENERIC_DB_ERROR)

