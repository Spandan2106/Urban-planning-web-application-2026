"""Greedy graph coloring implementation."""

from __future__ import annotations

import time
from typing import Any

import networkx as nx

from services.validator import validate_coloring


def greedy_coloring(graph: nx.Graph) -> dict[str, Any]:
    """Color a graph using NetworkX's largest-first greedy strategy."""

    start = time.perf_counter()
    raw_coloring = nx.coloring.greedy_color(graph, strategy="largest_first")
    coloring = {str(node): int(color) for node, color in raw_coloring.items()}
    valid, errors = validate_coloring(graph, coloring)
    elapsed = time.perf_counter() - start
    return {
        "algorithm": "Greedy",
        "coloring": coloring,
        "chromatic_number": len(set(coloring.values())),
        "execution_time": elapsed,
        "is_valid": valid,
        "errors": errors,
    }
