from fastapi import FastAPI
from app.notes import services as notes_services
from pydantic import BaseModel
from app.notes.schemas import (
Note,
NoteCreate,
NoteUpdate,
NotePatch
)
from typing import List
app = FastAPI()

# Dependency Injection
# from app.db.config import engine, get_db, get_async_session
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from fastapi import Depends
# @app.post("/notes", response_model=Note)
# async def create_note(note: NoteCreate, session: AsyncSession = Depends(get_db)):
#     return await notes_services.create_note(note)

@app.post("/notes")
async def create_note(note: NoteCreate) -> Note:
    note = await notes_services.create_note(note)
    return note

@app.get("/note/{note_id}")
async def get_note(note_id: int) -> Note:
    note = await notes_services.get_note(note_id)
    return note

@app.get("/notes")
async def get_all_notes() -> List[Note]:
    notes = await notes_services.get_all_notes()
    return notes

@app.put("/note/{note_id}")
async def update_note(note_id: int, note: NoteUpdate) -> Note:
    note = await notes_services.update_note(note_id, note)
    return note

@app.patch("/note/{note_id}")
async def patch_note(note_id: int, note: NotePatch):
    note = await notes_services.patch_note(note_id, note)
    return note

@app.delete("/note/{note_id}")
async def delete_note(note_id: int):
    return await notes_services.delete_note(note_id)