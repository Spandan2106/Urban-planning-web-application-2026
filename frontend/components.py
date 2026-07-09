"""Reusable Streamlit UI components."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st


def render_downloads(paths: dict[str, Path]) -> None:
    """Render download buttons for exported files."""

    labels = {
        "csv": "Download CSV",
        "excel": "Download Excel",
        "pdf": "Download PDF",
        "png": "Download PNG Graph",
    }
    mime_types = {
        "csv": "text/csv",
        "excel": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "pdf": "application/pdf",
        "png": "image/png",
    }
    columns = st.columns(len(paths))
    for index, (kind, path) in enumerate(paths.items()):
        with columns[index]:
            st.download_button(
                labels.get(kind, f"Download {kind}"),
                data=path.read_bytes(),
                file_name=path.name,
                mime=mime_types.get(kind, "application/octet-stream"),
                use_container_width=True,
            )


def require_analysis() -> dict[str, Any] | None:
    """Return the latest analysis from session state or show a prompt."""

    analysis = st.session_state.get("analysis")
    if not analysis:
        st.info("Upload and process a graph dataset to view this page.")
        return None
    return analysis
