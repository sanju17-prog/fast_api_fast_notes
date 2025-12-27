from app.db.config import async_session
from app.notes.models import Note as NoteModel
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import (
    NoteCreate,
    NoteUpdate,
    NotePatch
)

async def create_note(new_note: NoteCreate):
    async with async_session() as session:
        note = NoteModel(title=new_note.title, content=new_note.content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note

async def get_note(note_id: int):
    async with async_session() as session:
        note = await session.get(NoteModel, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

async def get_all_notes():
    async with async_session() as session:
        stmt = select(NoteModel)
        result = await session.execute(stmt)
        return result.scalars().all()

async def update_note(note_id: int, note_update: NoteUpdate):
    async with async_session() as session:
        note = await session.get(NoteModel, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = note_update.title
        note.content = note_update.content
        await session.commit()
        await session.refresh(note)
        return note

async def patch_note(note_id: int, note_patch: NotePatch):
    async with async_session() as session:
        note = await session.get(NoteModel, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        if note_patch.title is not None:
            note.title = note_patch.title
        if note_patch.content is not None:
            note.content = note_patch.content
        await session.commit()
        await session.refresh(note)
        return note

async def delete_note(note_id: int):
    async with async_session() as session:
        note = await session.get(NoteModel, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return True