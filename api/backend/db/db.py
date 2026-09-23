import sqlite3

# Import Path of db
from utils.constants import DB_PATH, DB_SONGS_TABLE

# Bring in helper
from .db_helpers.connect import connect_to_db
from .db_helpers.insert import insert_test

import asyncio # for testing

# Deciding what pattern to follow, singleton or conneciton pooling?
# singleton is good but can rely on itght coupling, which means we will need to pass
# db obje everywhere which is not very scalable and adds complexity quickly.

# Connection pooling is being researched - very scalable a bit more effort, will skip in favour of dependency injection.

# Must make this a database class and can use helpers for easier maintianability.


class Database:
	def __init__(self, db_path=DB_PATH):
		self.conn, self.cursor = connect_to_db()
		
	async def query(self, query, params=None):
		self.cursor.execute(query, params or ())
		return self.cursor.fetchall()
		
	async def insert_song(self, song_id, des):
		insert_test(self.conn, self.cursor, song_id, des)
	
	async def save(self):
		self.cursor.commit()
	
	async def close(self):
		self.conn.close()
	



database_instance = Database()

# DI funciton
async def get_db():
	try:
		print(f"databse type:  {type(database_instance)}")
		yield database_instance
	finally:
		print("Closing database after failing to grab db instance!")
		await database_instance.close()
		

async def main():
		
	# DB instance
	database_instance = Database() # test with this class first. Next time, change songs to match 
	# await get_db() # is an async generator as FastAPI handles these for DI
	
	# Next time add pydantic songs to insert them into database
	# Pydantic model to create SQL!
	# Add DB CRUD
	# Begin to add DB logic to file (basic query and adding basic data)
	# We will then focus on id3
	# Then how we will move the file!

	# db testing
	#db insert song
	await database_instance.insert_song('test 6', 'NOTHER BIG D')


	# Query db to see if it works
	query = f"SELECT * FROM {DB_SONGS_TABLE}"
	res =  await database_instance.query(query)
	print(f"Query DB: {res}")

	# close this when finished.
	await database_instance.close()
# test db
if __name__ == "__main__":
	asyncio.run(main())
