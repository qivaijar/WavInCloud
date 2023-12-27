from os.path import exists

from database import db_models
from database.db_engine import DatabaseEngine
from sqlmodel import SQLModel
from yaml import FullLoader, load


def create_db_and_tables(database_name: str):
    """Create SQLite database and start the engine

    Args:
        engine: Database engine object that handles the communication with the database
    """
    db_engine = DatabaseEngine(database_name)
    SQLModel.metadata.create_all(db_engine.engine)


if __name__ == "__main__":

    # Load base configs
    with open("base_conf.yaml", "r") as conf:
        conf_data = load(conf, Loader=FullLoader)

    # Create database file if not exists
    database_name = conf_data["database_name"]
    if not exists(database_name):
        create_db_and_tables(database_name)
