"""Runtime settings loaded from environment variables."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    """Container for application configuration."""

    app_name: str = os.getenv("APP_NAME", "Graph Coloring Web Application")
    mongodb_uri: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    mongodb_name: str = os.getenv("MONGODB_DB", "graph_coloring")
    uploads_dir: Path = BASE_DIR / "uploads"
    outputs_dir: Path = BASE_DIR / "outputs"
    assets_dir: Path = BASE_DIR / "assets"
    log_file: Path = BASE_DIR / "logs" / "app.log"


settings = Settings()
