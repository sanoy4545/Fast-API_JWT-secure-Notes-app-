from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models import User, Note
from db.session import session_local
from dependencies import get_user
from schemas import NoteCreate
from .auth import get_db

router = APIRouter()

@router.get("/notes")
def get_notes(current_user: str = Depends(get_user), db: Session = Depends(get_db)):
    # Find the User object from the username
    user = db.query(User).filter(User.username == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch all notes that belong to this user
    notes = db.query(Note).filter(Note.user_id == user.id).all()
    
    return notes
@router.post("/notes")
def add_note(note: NoteCreate, current_user: str = Depends(get_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {"msg": "Note added successfully", "note": {
        "id": new_note.id,
        "title": new_note.title,
        "content": new_note.content
    }}
