from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SnippetCreate(BaseModel):
    content: str
    is_public: bool = True
    expires_at: Optional[datetime] = None  # ✅ Correct way to allow None

class SnippetResponse(BaseModel):
    id: int
    content: str
    link: str
    is_public: bool = True
    expires_at: Optional[datetime] = None  # ✅ Fixes validation error
    created_at: datetime
