"""Service-facing API functions used by the Streamlit pages."""

from __future__ import annotations

from typing import Any

from models.dataset_model import create_dataset
from models.region_model import create_region_graph
from models.result_model import create_result
from services.backtracking import backtracking_coloring
from services.coloring import greedy_coloring
from services.graph_builder import build_graph, graph_to_payload
from services.parser import parse_graph_text
from services.statistics import graph_statistics


def process_graph_dataset(name: str, content: str, algorithm: str) -> dict[str, Any]:
    """Parse, build, color, validate, and persist a graph dataset."""

    nodes, edges = parse_graph_text(content)
    graph = build_graph(nodes, edges)
    dataset_id = create_dataset(name, content, nodes, edges)
    region_graph_id = create_region_graph(dataset_id, graph_to_payload(graph))
    if algorithm == "Backtracking":
        result = backtracking_coloring(graph)
    else:
        result = greedy_coloring(graph)
    result_id = create_result(dataset_id, region_graph_id, result)
    return {
        "dataset_id": dataset_id,
        "region_graph_id": region_graph_id,
        "result_id": result_id,
        "graph": graph,
        "result": result,
        "stats": graph_statistics(graph),
    }
