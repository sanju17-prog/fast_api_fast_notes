from typing import Optional
from pydantic import BaseModel, ConfigDict

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NotePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class Note(NoteBase):
    id: int
    model_config = ConfigDict(
        from_attributes = True
    )