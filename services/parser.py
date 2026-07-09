"""TXT graph parser."""

from __future__ import annotations

from pathlib import Path


class GraphParseError(ValueError):
    """Raised when a graph text file cannot be parsed."""


def _strip_comment(line: str) -> str:
    """Remove inline comments from a dataset line."""

    return line.split("#", 1)[0].strip()


def parse_graph_text(text: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Parse graph text into nodes and undirected edges.

    Supported lines are either `A B`, `A,B`, `A: B C D`, or a single node name.
    Empty lines and comments beginning with `#` are ignored.
    """

    nodes: set[str] = set()
    edges: set[tuple[str, str]] = set()

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = _strip_comment(raw_line)
        if not line:
            continue

        if ":" in line:
            source, neighbor_text = line.split(":", 1)
            source = source.strip()
            neighbors = neighbor_text.replace(",", " ").split()
            if not source:
                raise GraphParseError(f"Missing node name on line {line_number}.")
            nodes.add(source)
            for neighbor in neighbors:
                if neighbor == source:
                    continue
                nodes.add(neighbor)
                edges.add(tuple(sorted((source, neighbor))))
            continue

        parts = line.replace(",", " ").split()
        if len(parts) == 1:
            nodes.add(parts[0])
        elif len(parts) == 2:
            left, right = parts
            if left != right:
                nodes.update((left, right))
                edges.add(tuple(sorted((left, right))))
        else:
            raise GraphParseError(
                f"Line {line_number} must contain one node, one edge, or adjacency list."
            )

    if not nodes:
        raise GraphParseError("The graph file did not contain any nodes.")

    return sorted(nodes), sorted(edges)


def parse_graph_file(path: str | Path) -> tuple[list[str], list[tuple[str, str]]]:
    """Parse a graph from a text file path."""

    return parse_graph_text(Path(path).read_text(encoding="utf-8"))
