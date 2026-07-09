"""Coloring validation algorithms."""

from __future__ import annotations

import networkx as nx


def validate_coloring(graph: nx.Graph, coloring: dict[str, int]) -> tuple[bool, list[str]]:
    """Validate that all nodes are colored and adjacent nodes differ."""

    errors: list[str] = []
    for node in graph.nodes():
        if str(node) not in coloring:
            errors.append(f"Node {node} is missing a color.")

    for left, right in graph.edges():
        left_key = str(left)
        right_key = str(right)
        if coloring.get(left_key) == coloring.get(right_key):
            errors.append(f"Adjacent nodes {left} and {right} share a color.")

    return not errors, errors
