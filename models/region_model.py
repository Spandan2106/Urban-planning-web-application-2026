"""CRUD operations for region graph documents."""

from __future__ import annotations

from typing import Any

from config.database import mongo
from utils.constants import REGION_COLLECTION
from utils.helpers import new_id, serialize_document, utc_now

_memory_store: dict[str, dict[str, Any]] = {}


def create_region_graph(dataset_id: str, graph_payload: dict[str, Any]) -> str:
    """Create a region graph document and return its identifier."""

    document = {
        "region_graph_id": new_id(),
        "dataset_id": dataset_id,
        "graph": graph_payload,
        "created_at": utc_now(),
    }
    if mongo.is_available():
        mongo.collection(REGION_COLLECTION).insert_one(document)
    else:
        _memory_store[document["region_graph_id"]] = document
    return document["region_graph_id"]


def get_region_graph(region_graph_id: str) -> dict[str, Any] | None:
    """Return one region graph document."""

    if mongo.is_available():
        doc = mongo.collection(REGION_COLLECTION).find_one({"region_graph_id": region_graph_id})
        return serialize_document(doc) if doc else None
    return _memory_store.get(region_graph_id)


def list_region_graphs() -> list[dict[str, Any]]:
    """Return all region graph documents."""

    if mongo.is_available():
        return [serialize_document(doc) for doc in mongo.collection(REGION_COLLECTION).find()]
    return list(_memory_store.values())


def update_region_graph(region_graph_id: str, updates: dict[str, Any]) -> bool:
    """Update a region graph document."""

    if mongo.is_available():
        result = mongo.collection(REGION_COLLECTION).update_one(
            {"region_graph_id": region_graph_id}, {"$set": updates}
        )
        return result.modified_count > 0
    if region_graph_id in _memory_store:
        _memory_store[region_graph_id].update(updates)
        return True
    return False


def delete_region_graph(region_graph_id: str) -> bool:
    """Delete a region graph document."""

    if mongo.is_available():
        return mongo.collection(REGION_COLLECTION).delete_one({"region_graph_id": region_graph_id}).deleted_count > 0
    return _memory_store.pop(region_graph_id, None) is not None
