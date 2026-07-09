"""Tests for coloring validation."""

from __future__ import annotations

from services.graph_builder import build_graph
from services.validator import validate_coloring


def test_validate_coloring_success() -> None:
    """Validator should accept valid assignments."""

    graph = build_graph(["A", "B"], [("A", "B")])
    valid, errors = validate_coloring(graph, {"A": 0, "B": 1})
    assert valid is True
    assert errors == []


def test_validate_coloring_conflict() -> None:
    """Validator should reject adjacent nodes with equal colors."""

    graph = build_graph(["A", "B"], [("A", "B")])
    valid, errors = validate_coloring(graph, {"A": 0, "B": 0})
    assert valid is False
    assert errors
