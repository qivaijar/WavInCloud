from os.path import exists

from database import db_models
from database.db_engine import DatabaseEngine
from sqlmodel import SQLModel
from dotenv import load_dotenv
from os import getenv


def create_db_and_tables(database_name: str):
    """Create SQLite database and start the engine

    Args:
        engine: Database engine object that handles the communication with the database
    """
    db_engine = DatabaseEngine(database_name)
    SQLModel.metadata.create_all(db_engine.engine)


if __name__ == "__main__":

    # Get db name from .env file
    load_dotenv()
    database_name = getenv('DB_NAME')

    # Create database file if not exists
    if not exists(database_name):
        create_db_and_tables(database_name)
