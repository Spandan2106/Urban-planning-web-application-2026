"""Tests for graph coloring algorithms."""

from __future__ import annotations

from services.backtracking import backtracking_coloring
from services.coloring import greedy_coloring
from services.graph_builder import build_graph


def test_greedy_coloring_is_valid() -> None:
    """Greedy coloring should produce a valid result."""

    graph = build_graph(["A", "B", "C"], [("A", "B"), ("B", "C"), ("A", "C")])
    result = greedy_coloring(graph)
    assert result["is_valid"] is True
    assert result["chromatic_number"] == 3


def test_backtracking_coloring_is_valid() -> None:
    """Backtracking coloring should produce an optimal triangle coloring."""

    graph = build_graph(["A", "B", "C"], [("A", "B"), ("B", "C"), ("A", "C")])
    result = backtracking_coloring(graph)
    assert result["is_valid"] is True
    assert result["chromatic_number"] == 3
