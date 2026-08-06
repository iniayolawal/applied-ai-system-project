from pathlib import Path

from logger_utils import log_hint_event


def test_log_hint_event_writes_expected_fields(tmp_path):
    log_path = tmp_path / "hints.log"

    entry_path = log_hint_event(
        guess=42,
        secret=50,
        category="slightly_low",
        hint="Try a slightly higher guess.",
        validation_result=True,
        log_path=log_path,
    )

    assert Path(entry_path) == log_path
    content = log_path.read_text(encoding="utf-8")
    assert "guess=42" in content
    assert "secret=50" in content
    assert "category=slightly_low" in content
    assert "hint=Try a slightly higher guess." in content
    assert "validation_result=PASS" in content
