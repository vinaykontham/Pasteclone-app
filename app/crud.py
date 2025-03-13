from sqlalchemy.orm import Session
from app.models import Snippet
from app.utils import generate_unique_link

def create_snippet(db: Session, snippet_data):
    link = generate_unique_link()
    db_snippet = Snippet(
        content=snippet_data.content,
        link=link,
        is_public=snippet_data.is_public,
        expires_at=snippet_data.expires_at,
    )
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet

def get_snippet_by_link(db: Session, link: str):
    return db.query(Snippet).filter(Snippet.link == link).first()