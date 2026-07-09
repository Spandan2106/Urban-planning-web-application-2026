"""Tests for graph building and statistics."""

from __future__ import annotations

from services.graph_builder import build_graph, graph_to_payload
from services.statistics import graph_statistics


def test_build_graph_payload() -> None:
    """Graph builder should preserve nodes and edges."""

    graph = build_graph(["A", "B"], [("A", "B")])
    payload = graph_to_payload(graph)
    assert payload["total_nodes"] == 2
    assert payload["total_edges"] == 1


def test_graph_statistics() -> None:
    """Statistics should include expected counts."""

    graph = build_graph(["A", "B", "C"], [("A", "B")])
    stats = graph_statistics(graph)
    assert stats["total_nodes"] == 3
    assert stats["connected_components"] == 2
