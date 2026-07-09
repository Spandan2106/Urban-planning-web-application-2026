"""Tests for graph parsing."""

from __future__ import annotations

import pytest

from services.parser import GraphParseError, parse_graph_text


def test_parse_adjacency_list() -> None:
    """Parser should handle adjacency-list syntax."""

    nodes, edges = parse_graph_text("A: B C\nB: C")
    assert nodes == ["A", "B", "C"]
    assert edges == [("A", "B"), ("A", "C"), ("B", "C")]


def test_parse_rejects_empty_input() -> None:
    """Parser should reject files without nodes."""

    with pytest.raises(GraphParseError):
        parse_graph_text("# only comments")
