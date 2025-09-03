# Example sync job outline.
from sqlalchemy.orm import Session
from app.models import Vendor, Product
from app.services import shopify, printful

async def sync_shopify(db: Session):
    # Ensure vendor row exists
    vendor = db.query(Vendor).filter_by(name="default-shopify").first()
    if not vendor:
        vendor = Vendor(name="default-shopify", platform="shopify")
        db.add(vendor); db.commit(); db.refresh(vendor)

    products = await shopify.fetch_products(limit=25)
    for p in products:
        existing = db.query(Product).filter_by(vendor_id=vendor.id, external_id=p["external_id"]).first()
        if existing:
            existing.title = p["title"]
            existing.description = p.get("description")
        else:
            db.add(Product(
                vendor_id=vendor.id,
                external_id=p["external_id"],
                title=p["title"],
                description=p.get("description"),
            ))
    db.commit()

async def sync_printful(db: Session):
    vendor = db.query(Vendor).filter_by(name="default-printful").first()
    if not vendor:
        vendor = Vendor(name="default-printful", platform="printful")
        db.add(vendor); db.commit(); db.refresh(vendor)

    items = await printful.fetch_store_products(limit=25)
    for it in items:
        existing = db.query(Product).filter_by(vendor_id=vendor.id, external_id=it["external_id"]).first()
        if existing:
            existing.title = it["title"]
            existing.description = it.get("description")
        else:
            db.add(Product(
                vendor_id=vendor.id,
                external_id=it["external_id"],
                title=it["title"],
                description=it.get("description"),
            ))
    db.commit()
