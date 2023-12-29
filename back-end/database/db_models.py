from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class AudioData(SQLModel, table=True):
    file_id: UUID = Field(default=uuid4, primary_key=True)
    title: str = Field(index=True, unique=True)
    alternative_title: Optional[str] = Field(index=True, unique=True)
    artist: str = Field(index=True)
    genre: Optional[str] = None
    lyric: Optional[str] = None
    file_path: str = Field(unique=True)
    added_at: str
