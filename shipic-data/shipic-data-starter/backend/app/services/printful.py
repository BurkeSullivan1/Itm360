import httpx
from typing import Any, Dict, List
from app.config import settings

BASE_URL = "https://api.printful.com"

async def fetch_store_products(limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
    """
    Minimal Printful example (requires API key).
    """
    if not settings.printful_api_key:
        return []

    headers = {"Authorization": f"Bearer {settings.printful_api_key}"}
    url = f"{BASE_URL}/store/products?limit={limit}&offset={offset}"

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        result = data.get("result", [])
        products = []
        for item in result:
            products.append({
                "external_id": str(item.get("id")),
                "title": item.get("name"),
                "description": (item.get("external_id") or ""),
            })
        return products
