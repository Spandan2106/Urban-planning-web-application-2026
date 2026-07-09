"""General helper functions."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


def utc_now() -> datetime:
    """Return the current UTC datetime."""

    return datetime.now(timezone.utc)


def new_id() -> str:
    """Return a unique string identifier."""

    return uuid4().hex


def serialize_document(document: dict[str, Any]) -> dict[str, Any]:
    """Convert MongoDB-specific values into display-friendly strings."""

    serialized = dict(document)
    if "_id" in serialized:
        serialized["_id"] = str(serialized["_id"])
    return serialized
