# Placeholder for Google Trends integration.
# In production, consider pytrends or a first-party Trends API when available.
# Here we just mock a response.
from typing import List, Dict

def related_trending_terms(keyword: str, geo: str = "US") -> List[Dict]:
    # TODO: integrate pytrends and return real interest_over_time/related_queries
    demo = [
        {"term": f"{keyword} minimalist", "score": 87},
        {"term": f"{keyword} aesthetic", "score": 73},
        {"term": f"{keyword} 2025", "score": 61},
    ]
    return demo
