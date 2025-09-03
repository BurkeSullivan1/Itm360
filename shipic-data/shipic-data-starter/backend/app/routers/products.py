from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db, Base, engine
from app.models import Product
from app.schemas import ProductOut

router = APIRouter()

# Simple auto-migration for dev convenience (use Alembic later)
Base.metadata.create_all(bind=engine)

@router.get("", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).limit(100).all()
