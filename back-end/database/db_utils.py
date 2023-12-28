from sqlmodel import create_engine, SQLModel

def create_db_engine(database_path: str):
    database_url = f"sqlite:///{database_path}"
    return create_engine(database_url, echo=True)

def create_db_and_tables(database_engine):
    SQLModel.metadata.create_all(database_engine)
