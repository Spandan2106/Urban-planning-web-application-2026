"""Export graph coloring results to common formats."""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from services.visualization import save_graph_png


def coloring_dataframe(coloring: dict[str, int]) -> pd.DataFrame:
    """Return a DataFrame containing nodes and assigned colors."""

    rows = [{"Region": node, "Category": color + 1} for node, color in sorted(coloring.items())]
    return pd.DataFrame(rows)


def export_csv(coloring: dict[str, int], path: Path) -> Path:
    """Export coloring results as CSV."""

    path.parent.mkdir(parents=True, exist_ok=True)
    coloring_dataframe(coloring).to_csv(path, index=False)
    return path


def export_excel(coloring: dict[str, int], path: Path) -> Path:
    """Export coloring results as an Excel workbook."""

    path.parent.mkdir(parents=True, exist_ok=True)
    coloring_dataframe(coloring).to_excel(path, index=False)
    return path


def export_pdf(
    graph: nx.Graph, result: dict[str, object], stats: dict[str, object], path: Path
) -> Path:
    """Export a PDF report for the graph coloring result."""

    path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(path), pagesize=letter)
    styles = getSampleStyleSheet()
    elements: list[object] = [
        Paragraph("Graph Coloring Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Algorithm: {result['algorithm']}", styles["Normal"]),
        Paragraph(f"Chromatic number: {result['chromatic_number']}", styles["Normal"]),
        Paragraph(f"Execution time: {float(result['execution_time']):.6f} seconds", styles["Normal"]),
        Paragraph(f"Valid coloring: {result['is_valid']}", styles["Normal"]),
        Spacer(1, 12),
        Paragraph("Graph Statistics", styles["Heading2"]),
    ]

    stats_rows = [[key.replace("_", " ").title(), value] for key, value in stats.items()]
    stats_table = Table([["Metric", "Value"], *stats_rows])
    stats_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2f80ed")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ]
        )
    )
    elements.extend([stats_table, Spacer(1, 12), Paragraph("Assignments", styles["Heading2"])])

    coloring = result["coloring"]
    if isinstance(coloring, dict):
        assignment_rows = [["Region", "Category"]]
        assignment_rows.extend([[node, color + 1] for node, color in sorted(coloring.items())])
        table = Table(assignment_rows)
        table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.grey)]))
        elements.append(table)

    document.build(elements)
    return path


def export_all(
    graph: nx.Graph, result: dict[str, object], stats: dict[str, object], output_dir: Path
) -> dict[str, Path]:
    """Export all supported artifact types and return their paths."""

    coloring = result["coloring"]
    if not isinstance(coloring, dict):
        raise TypeError("Result coloring must be a dictionary.")

    return {
        "csv": export_csv(coloring, output_dir / "result.csv"),
        "excel": export_excel(coloring, output_dir / "result.xlsx"),
        "pdf": export_pdf(graph, result, stats, output_dir / "result.pdf"),
        "png": save_graph_png(graph, coloring, output_dir / "graph.png"),
    }
