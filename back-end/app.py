from os import getcwd, getenv
from os.path import exists, join

from database import db_models  # noqa
from database.db_utils import create_db_and_tables, create_db_engine
from dotenv import load_dotenv


def main():
    # Get db name from .env file
    load_dotenv("../.env")
    database_path = join(getcwd(), "database", getenv("DB_NAME"))

    # Initiate db engine
    db_engine = create_db_engine(database_path)

    # Create database file if not exists (based on db_models.py)
    if not exists(database_path):
        create_db_and_tables(db_engine)


if __name__ == "__main__":
    main()

# concept
# Backend will read a directory contains audio files
# Backend will create a database (if not exist yet), and save the audio data
# Backend will send the audio data, reading the file based on path as a buffer
# Frontend will process the sent buffer
# Need md5 sum checking to check if similar file with different name exists
