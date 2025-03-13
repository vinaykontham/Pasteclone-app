from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.config import get_db  # Ensure this import is correct

router = APIRouter()

@router.post("/", response_model=schemas.SnippetResponse)
def create_snippet(snippet: schemas.SnippetCreate, db: Session = Depends(get_db)):
    return crud.create_snippet(db, snippet)

@router.get("/{link}", response_model=schemas.SnippetResponse)
def read_snippet(link: str, db: Session = Depends(get_db)):
    snippet = crud.get_snippet_by_link(db, link)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet