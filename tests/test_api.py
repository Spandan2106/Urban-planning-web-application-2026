"""Tests for the service API."""

from __future__ import annotations

from routes.api import process_graph_dataset


def test_process_graph_dataset() -> None:
    """API should parse, color, and return persisted identifiers."""

    analysis = process_graph_dataset("unit.txt", "A B\nB C", "Greedy")
    assert analysis["dataset_id"]
    assert analysis["result"]["is_valid"] is True
    assert analysis["stats"]["total_edges"] == 2
