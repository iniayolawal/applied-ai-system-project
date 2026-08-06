from __future__ import annotations

from datetime import datetime, UTC
from pathlib import Path
from typing import Union


def log_hint_event(
    guess: int,
    secret: int,
    category: str,
    hint: str,
    validation_result: bool,
    log_path: Union[str, Path, None] = None,
) -> Path:
    """Append a single hint-generation event to a text log file."""
    if log_path is None:
        log_path = Path(__file__).resolve().parent / "hint_events.log"
    else:
        log_path = Path(log_path)

    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    status = "PASS" if validation_result else "FAILED"
    line = (
        f"timestamp={timestamp} | "
        f"guess={guess} | "
        f"secret={secret} | "
        f"category={category} | "
        f"hint={hint} | "
        f"validation_result={status}\n"
    )

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(line)

    return log_path
