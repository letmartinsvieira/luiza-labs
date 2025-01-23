# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
import os
import sqlalchemy as db
from sqlalchemy import create_engine

from app.database.orm_config.declarative_base import Base
from app.modules.client.infra.db.client_model import ClientModel

engine = db.create_engine('sqlite://service_client_db.db', echo=True)


db_url = os.environ['DATABASE_URL']

def get_connection():
	return create_engine(
		url=db_url
		)
	)
	
	
if __name__ == '__main__':

	try:
		# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
		engine = get_connection()
		print('CONNECTION --> ', engine)
		base = Base()
		metadata_obj = db.MetaData()
		base.metadata_obj.create_all(engine)
		print(
			f"Connection to the {host} for user {user} created successfully.")
    
	except Exception as ex:
		print("Connection could not be made due to the following error: \n", ex)
