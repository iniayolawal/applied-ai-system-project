import json
import random
from pathlib import Path
from typing import Dict, List


def load_hint_knowledge_base(path: str | None = None) -> Dict[str, dict]:
    """Load the JSON hint knowledge base from disk."""
    if path is None:
        path = Path(__file__).resolve().parent / "hint_knowledge_base.json"
    else:
        path = Path(path)

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("Hint knowledge base must be a JSON object")

    return data


def get_random_hint(category: str, knowledge_base: Dict[str, dict] | None = None) -> str:
    """Return a random hint string from the requested category."""
    if knowledge_base is None:
        knowledge_base = load_hint_knowledge_base()

    if category not in knowledge_base:
        raise KeyError(category)

    category_data = knowledge_base[category]
    hints = category_data.get("hints", [])

    if not hints:
        raise ValueError(f"Category '{category}' does not contain any hints")

    return random.choice(hints)
