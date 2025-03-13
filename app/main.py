from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import snippets
from app.config import Base, engine  # Import Base and engine from your config file

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Include snippet routes
app.include_router(snippets.router, prefix="/api/v1/snippets", tags=["snippets"])

# Homepage route
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Snippet page route
@app.get("/{link}")
def read_snippet_page(request: Request, link: str):
    return templates.TemplateResponse("snippet.html", {"request": request})