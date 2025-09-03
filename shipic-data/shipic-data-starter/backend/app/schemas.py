from pydantic import BaseModel
from datetime import datetime

class ProductOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    sku: str | None = None
    price: float | None = None
    currency: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
