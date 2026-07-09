"""Graph construction services."""

from __future__ import annotations

import networkx as nx


def build_graph(nodes: list[str], edges: list[tuple[str, str]]) -> nx.Graph:
    """Build and return an undirected NetworkX graph."""

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def graph_to_payload(graph: nx.Graph) -> dict[str, object]:
    """Convert a NetworkX graph into a serializable payload."""

    return {
        "nodes": sorted(str(node) for node in graph.nodes()),
        "edges": sorted((str(left), str(right)) for left, right in graph.edges()),
        "total_nodes": graph.number_of_nodes(),
        "total_edges": graph.number_of_edges(),
    }
