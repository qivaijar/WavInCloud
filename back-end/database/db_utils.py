from datetime import datetime
from typing import List

from db_models import AudioData
from sqlmodel import Session, SQLModel, create_engine


def create_db_engine(database_path: str):
    database_url = f"sqlite:///{database_path}"
    return create_engine(database_url, echo=True)


def create_db_and_tables(database_engine):
    SQLModel.metadata.create_all(database_engine)


def add_to_db(input_data: AudioData | List[AudioData], database_engine):
    if not isinstance(input_data, list):
        input_data = [input_data]

    with Session(database_engine) as session:
        [session.add(data) for data in input_data]
        session.commit()


def get_current_datetime():
    return datetime.now().strftime("%Y/%m/%d,%H:%M:%S")
