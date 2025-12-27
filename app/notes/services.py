from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException

async def create_note(title: str, content: str):
    async with async_session() as session:
        note = Note(title=title, content=content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note

async def get_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

async def get_all_notes():
    async with async_session() as session:
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()

async def update_note(note_id: int, title: str, content: str):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = title
        note.content = content
        await session.commit()
        await session.refresh(note)
        return note

async def patch_note(note_id: int, title: str, content: str):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = title if title else note.title
        note.content = content if content else note.content
        await session.commit()
        await session.refresh(note)
        return note

async def delete_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"message": "Note deleted successfully"}