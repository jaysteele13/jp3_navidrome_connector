import sqlite3

# Import Path of db
from utils.constants import DB_PATH 
from utils.classes import Song_Metadata

from sqlmodel import Session, SQLModel, create_engine, Field
from uuid import uuid4, UUID
# from sqlalchemy import Index




def connect_to_db():
	connect_args = {"check_same_thread": False}
	
	# if all ready created ignore
	engine = create_engine(DB_PATH, connect_args=connect_args)
	
	SQLModel.metadata.create_all(engine)
	
	return engine

