from typing import List

def suggest_title_seo(title: str) -> str:
    # TODO: replace with real AI module or rules
    return f"{title} | Premium Quality, Fast Shipping"

def suggest_tags(title: str) -> List[str]:
    base = [w.lower() for w in title.split() if len(w) > 3]
    return list(set(base + ["trending", "best-seller"]))
