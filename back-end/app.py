from os.path import exists

from database import db_models
from database.db_utils import create_db_engine, create_db_and_tables
from dotenv import load_dotenv
from os import getenv, getcwd
from os.path import join


if __name__ == "__main__":

    # Get db name from .env file
    load_dotenv('../.env')
    database_path = join(getcwd(), 'database', getenv('DB_NAME'))

    # Initiate db engine
    db_engine = create_db_engine(database_path)

    # Create database file if not exists (based on db_models.py)
    if not exists(database_path):
        create_db_and_tables(db_engine)