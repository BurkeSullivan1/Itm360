from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db import Base

class Vendor(Base):
    __tablename__ = "vendors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    platform: Mapped[str] = mapped_column(String(50))  # e.g. shopify, printful

    products = relationship("Product", back_populates="vendor")

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    external_id: Mapped[str] = mapped_column(String(128), index=True)  # platform product id
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(4000))
    sku: Mapped[str | None] = mapped_column(String(128), index=True)
    price: Mapped[float | None] = mapped_column(Float)
    currency: Mapped[str | None] = mapped_column(String(8))
    tags: Mapped[dict | None] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    vendor = relationship("Vendor", back_populates="products")

    __table_args__ = (
        UniqueConstraint("vendor_id", "external_id", name="uq_vendor_product"),
    )

class Trend(Base):
    __tablename__ = "trends"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source: Mapped[str] = mapped_column(String(50))  # google_trends, tiktok
    term: Mapped[str] = mapped_column(String(255), index=True)
    score: Mapped[float] = mapped_column(Float)  # normalized interest
    geo: Mapped[str | None] = mapped_column(String(10))
    captured_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class ProductTrendMatch(Base):
    __tablename__ = "product_trend_matches"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    trend_id: Mapped[int] = mapped_column(ForeignKey("trends.id"))
    relevance: Mapped[float] = mapped_column(Float)  # 0..1
    notes: Mapped[str | None] = mapped_column(String(1024))

    __table_args__ = (
        UniqueConstraint("product_id", "trend_id", name="uq_product_trend"),
    )
