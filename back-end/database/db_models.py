from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

class AudioInfo(SQLModel, table=True):
    file_id: UUID = Field(default=uuid4, primary_key=True)
    title: str = Field(index=True, unique=True)
    artist: str = Field(index=True)
    genre: Optional[str] = None
    lyric: Optional[str] = None
    file_path: str
    added_at: str
    
