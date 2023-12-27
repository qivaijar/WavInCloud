from typing import Optional

from sqlmodel import Field, SQLModel

class ExperimentInfo(SQLModel, table=True):
    experiment_id: Optional[str] = Field(default=None, primary_key=True)
    created_at: Optional[str] = None
    loss_value: float
    duration: float
    experiment_name: str
    Architecture: str
    author: str
    toolkit: str
    dataset: str
    short_description: str
    long_description: str

class File(SQLModel, table=True):
    file_id: Optional[str] = Field(default=None, primary_key=True)
    filename: Optional[str] = None
    description: Optional[str] = None
    tag: Optional[str] = None
    url: Optional[str] = None
