from pydantic import BaseModel
from datetime import datetime

class SnippetCreate(BaseModel):
    content: str
    is_public: bool = True
    expires_at: datetime = None 
    

class SnippetResponse(BaseModel):
    id: int
    content: str
    link: str
    is_public: bool = True
    expires_at: datetime = None
    created_at: datetime