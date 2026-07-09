"""Backtracking graph coloring implementation."""

from __future__ import annotations

import time
from typing import Any

import networkx as nx

from services.validator import validate_coloring
from utils.constants import MAX_BACKTRACKING_COLORS


def _is_safe(
    graph: nx.Graph, node: str, color: int, assignments: dict[str, int]
) -> bool:
    """Return True when assigning a color does not conflict with neighbors."""

    return all(assignments.get(str(neighbor)) != color for neighbor in graph.neighbors(node))


def _solve(
    graph: nx.Graph,
    ordered_nodes: list[str],
    color_count: int,
    assignments: dict[str, int],
    deadline: float,
) -> bool:
    """Recursively try to color all nodes with a fixed number of colors."""

    if len(assignments) == len(ordered_nodes):
        return True

    if time.perf_counter() > deadline:
        return False

    node = ordered_nodes[len(assignments)]
    for color in range(color_count):
        if _is_safe(graph, node, color, assignments):
            assignments[node] = color
            if _solve(graph, ordered_nodes, color_count, assignments, deadline):
                return True
            assignments.pop(node, None)
    return False


def backtracking_coloring(
    graph: nx.Graph, timeout_seconds: int = 5
) -> dict[str, Any]:
    """Find a valid coloring by incrementally trying color counts."""

    start = time.perf_counter()
    deadline = start + timeout_seconds
    ordered_nodes = [str(node) for node, _ in sorted(graph.degree, key=lambda item: item[1], reverse=True)]
    limit = min(max(graph.number_of_nodes(), 1), MAX_BACKTRACKING_COLORS)
    coloring: dict[str, int] = {}

    for color_count in range(1, limit + 1):
        attempt: dict[str, int] = {}
        if _solve(graph, ordered_nodes, color_count, attempt, deadline):
            coloring = attempt
            break

        if time.perf_counter() > deadline:
            break

    timed_out = not coloring and (time.perf_counter() > deadline)
    if not coloring:
        coloring = nx.coloring.greedy_color(graph, strategy="largest_first")
        coloring = {str(node): int(color) for node, color in coloring.items()}

    valid, errors = validate_coloring(graph, coloring)
    elapsed = time.perf_counter() - start
    return {
        "algorithm": "Backtracking",
        "coloring": coloring,
        "chromatic_number": len(set(coloring.values())),
        "execution_time": elapsed,
        "is_valid": valid,
        "errors": errors,
        "timed_out": timed_out,
    }
