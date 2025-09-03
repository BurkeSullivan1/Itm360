import httpx
from typing import Any, Dict, List, Optional
from app.config import settings

SHOPIFY_GRAPHQL_URL = (
    f"https://{settings.shopify_store_domain}/admin/api/2024-04/graphql.json"
    if settings.shopify_store_domain else None
)

async def fetch_products(limit: int = 50) -> List[Dict[str, Any]]:
    """
    Minimal Shopify GraphQL example (requires Admin API access token).
    Returns a list of product dicts with title, id, variants, etc.
    """
    if not SHOPIFY_GRAPHQL_URL or not settings.shopify_admin_api_access_token:
        return []

    query = {
        "query": f"""
        {{
          products(first: {limit}) {{
            edges {{
              node {{
                id
                title
                description
                variants(first: 10) {{
                  edges {{
                    node {{ id sku price }}
                  }}
                }}
              }}
            }}
          }}
        }}
        """
    }

    headers = {
        "X-Shopify-Access-Token": settings.shopify_admin_api_access_token,
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(SHOPIFY_GRAPHQL_URL, json=query, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        edges = data.get("data", {}).get("products", {}).get("edges", [])
        products: List[Dict[str, Any]] = []
        for e in edges:
            node = e["node"]
            products.append({
                "external_id": node["id"],
                "title": node["title"],
                "description": node.get("description"),
                "variants": [v["node"] for v in node.get("variants", {}).get("edges", [])]
            })
        return products
