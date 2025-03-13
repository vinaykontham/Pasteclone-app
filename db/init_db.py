# db/init_db.py
from app.config import engine, Base

def init_db():
    # Create all tables defined in the models
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")