from sqlmodel import create_engine

class DatabaseEngine:
    def __init__(self, database_name: str):
        database_url = f"sqlite:///{database_name}"
        self.engine = create_engine(database_url, echo=True)
