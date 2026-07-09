"""Seed sample graph datasets into MongoDB when available."""

from __future__ import annotations

from pathlib import Path

from models.dataset_model import create_dataset
from services.parser import parse_graph_text


def seed_samples(sample_dir: Path | None = None) -> list[str]:
    """Seed all sample TXT files and return created dataset identifiers."""

    base_dir = sample_dir or Path(__file__).resolve().parents[1] / "sample_data"
    created: list[str] = []
    for sample_file in sorted(base_dir.glob("*.txt")):
        content = sample_file.read_text(encoding="utf-8")
        nodes, edges = parse_graph_text(content)
        created.append(create_dataset(sample_file.name, content, nodes, edges))
    return created


if __name__ == "__main__":
    print(seed_samples())
