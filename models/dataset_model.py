"""CRUD operations for graph datasets."""

from __future__ import annotations

from typing import Any

from pymongo.errors import PyMongoError

from config.database import mongo
from utils.constants import DATASET_COLLECTION
from utils.helpers import new_id, serialize_document, utc_now

_memory_store: dict[str, dict[str, Any]] = {}


def create_dataset(name: str, content: str, nodes: list[str], edges: list[tuple[str, str]]) -> str:
    """Create a dataset document and return its identifier."""

    document = {
        "dataset_id": new_id(),
        "name": name,
        "content": content,
        "nodes": nodes,
        "edges": edges,
        "created_at": utc_now(),
    }
    if mongo.is_available():
        mongo.collection(DATASET_COLLECTION).insert_one(document)
    else:
        _memory_store[document["dataset_id"]] = document
    return document["dataset_id"]


def get_dataset(dataset_id: str) -> dict[str, Any] | None:
    """Return one dataset document by identifier."""

    if mongo.is_available():
        result = mongo.collection(DATASET_COLLECTION).find_one({"dataset_id": dataset_id})
        return serialize_document(result) if result else None
    return _memory_store.get(dataset_id)


def list_datasets() -> list[dict[str, Any]]:
    """Return all dataset documents."""

    if mongo.is_available():
        return [serialize_document(doc) for doc in mongo.collection(DATASET_COLLECTION).find()]
    return list(_memory_store.values())


def update_dataset(dataset_id: str, updates: dict[str, Any]) -> bool:
    """Update a dataset document."""

    if mongo.is_available():
        result = mongo.collection(DATASET_COLLECTION).update_one(
            {"dataset_id": dataset_id}, {"$set": updates}
        )
        return result.modified_count > 0
    if dataset_id in _memory_store:
        _memory_store[dataset_id].update(updates)
        return True
    return False


def delete_dataset(dataset_id: str) -> bool:
    """Delete a dataset document."""

    try:
        if mongo.is_available():
            return mongo.collection(DATASET_COLLECTION).delete_one({"dataset_id": dataset_id}).deleted_count > 0
    except PyMongoError:
        return False
    return _memory_store.pop(dataset_id, None) is not None
