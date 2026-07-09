"""Graph visualization helpers."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(__file__).resolve().parents[1] / ".matplotlib"),
)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.patches import Patch

from utils.constants import DEFAULT_COLORS


def color_values(coloring: dict[str, int], nodes: Iterable[str]) -> list[str]:
    """Return display colors for nodes in graph order."""

    return [DEFAULT_COLORS[coloring.get(str(node), 0) % len(DEFAULT_COLORS)] for node in nodes]


def create_graph_figure(graph: nx.Graph, coloring: dict[str, int] | None = None) -> Figure:
    """Create a Matplotlib figure for a graph and optional coloring."""

    figure, axis = plt.subplots(figsize=(9, 6))
    # Increase k for more space between nodes and reduce iterations for speed.
    k = 1.5 / (graph.number_of_nodes() ** 0.5) if graph.number_of_nodes() > 0 else 1.0
    iterations = 30 if graph.number_of_nodes() > 50 else 50
    pos = nx.spring_layout(graph, seed=42, k=k, iterations=iterations)

    coloring = coloring or {}
    node_colors = color_values(coloring, graph.nodes())

    nx.draw_networkx_nodes(
        graph, pos, node_color=node_colors, node_size=900, alpha=0.9, ax=axis
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        width=1.8,
        edge_color="#7f8c8d",
        arrows=True,
        arrowstyle="-",
        connectionstyle="arc3,rad=0.1",
        ax=axis,
    )
    nx.draw_networkx_labels(graph, pos, font_color="white", font_weight="bold", ax=axis)

    used_colors = sorted(set(coloring.values())) if coloring else [0]
    legend = [
        Patch(facecolor=DEFAULT_COLORS[color % len(DEFAULT_COLORS)], label=f"Category {color + 1}")
        for color in used_colors
    ]
    axis.legend(handles=legend, loc="upper right")
    axis.set_axis_off()
    figure.tight_layout()
    return figure


def save_graph_png(graph: nx.Graph, coloring: dict[str, int], path: Path) -> Path:
    """Save a graph visualization as a PNG file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    figure = create_graph_figure(graph, coloring)
    figure.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(figure)
    return path
