"""CRUD operations for graph coloring results."""

from __future__ import annotations

from typing import Any

from config.database import mongo
from utils.constants import RESULT_COLLECTION
from utils.helpers import new_id, serialize_document, utc_now

_memory_store: dict[str, dict[str, Any]] = {}


def create_result(dataset_id: str, region_graph_id: str, result: dict[str, Any]) -> str:
    """Create a coloring result document and return its identifier."""

    document = {
        "result_id": new_id(),
        "dataset_id": dataset_id,
        "region_graph_id": region_graph_id,
        "result": result,
        "created_at": utc_now(),
    }
    if mongo.is_available():
        mongo.collection(RESULT_COLLECTION).insert_one(document)
    else:
        _memory_store[document["result_id"]] = document
    return document["result_id"]


def get_result(result_id: str) -> dict[str, Any] | None:
    """Return one coloring result document."""

    if mongo.is_available():
        doc = mongo.collection(RESULT_COLLECTION).find_one({"result_id": result_id})
        return serialize_document(doc) if doc else None
    return _memory_store.get(result_id)


def list_results() -> list[dict[str, Any]]:
    """Return all coloring result documents."""

    if mongo.is_available():
        return [serialize_document(doc) for doc in mongo.collection(RESULT_COLLECTION).find()]
    return list(_memory_store.values())


def update_result(result_id: str, updates: dict[str, Any]) -> bool:
    """Update a coloring result document."""

    if mongo.is_available():
        result = mongo.collection(RESULT_COLLECTION).update_one(
            {"result_id": result_id}, {"$set": updates}
        )
        return result.modified_count > 0
    if result_id in _memory_store:
        _memory_store[result_id].update(updates)
        return True
    return False


def delete_result(result_id: str) -> bool:
    """Delete a coloring result document."""

    if mongo.is_available():
        return mongo.collection(RESULT_COLLECTION).delete_one({"result_id": result_id}).deleted_count > 0
    return _memory_store.pop(result_id, None) is not None
