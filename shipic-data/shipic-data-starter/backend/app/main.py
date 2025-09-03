
from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.products import router as products_router
from app.routers.intel import router as intel_router

app = FastAPI(title="Shipic Data API", version="0.1.0")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(intel_router)


@app.get("/")
def root():
    return {"ok": True, "service": "shippic-data"}
