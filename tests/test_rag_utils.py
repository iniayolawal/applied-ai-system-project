import pytest

from rag_utils import get_random_hint, load_hint_knowledge_base


def test_loads_hint_knowledge_base_from_workspace_file():
    data = load_hint_knowledge_base()
    assert isinstance(data, dict)
    assert "far_low" in data


def test_returns_random_hint_for_existing_category():
    hint = get_random_hint("far_low")
    assert isinstance(hint, str)
    assert hint


def test_raises_for_missing_category():
    with pytest.raises(KeyError, match="far_missing"):
        get_random_hint("far_missing")
