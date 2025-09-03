# app/workers/bootstrap_db.py
from app.db import Base, engine
import app.models  # ensure models are imported so tables are registered

def create_all():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_all()
