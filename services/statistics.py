"""Graph and database statistics services."""

from __future__ import annotations

from typing import Any

import networkx as nx
from pymongo.errors import PyMongoError

from config.database import mongo
from utils.constants import DATASET_COLLECTION, REGION_COLLECTION, RESULT_COLLECTION


def graph_statistics(graph: nx.Graph) -> dict[str, Any]:
    """Calculate common graph statistics."""

    components = nx.number_connected_components(graph) if graph.number_of_nodes() else 0
    density = nx.density(graph) if graph.number_of_nodes() > 1 else 0.0
    return {
        "total_nodes": graph.number_of_nodes(),
        "total_edges": graph.number_of_edges(),
        "connected_components": components,
        "density": round(float(density), 4),
        "average_degree": round(
            sum(dict(graph.degree()).values()) / graph.number_of_nodes(), 4
            if graph.number_of_nodes()
            else 0.0,
        ),
    }


def database_statistics() -> dict[str, int | str]:
    """Return document counts for each MongoDB collection."""

    if not mongo.is_available():
        return {"status": "offline", "datasets": 0, "regions": 0, "results": 0}
    try:
        database = mongo.database()
        return {
            "status": "online",
            "datasets": database[DATASET_COLLECTION].count_documents({}),
            "regions": database[REGION_COLLECTION].count_documents({}),
            "results": database[RESULT_COLLECTION].count_documents({}),
        }
    except PyMongoError:
        return {"status": "offline", "datasets": 0, "regions": 0, "results": 0}
