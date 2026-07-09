"""Results page."""

from __future__ import annotations

import streamlit as st

from config.settings import settings
from frontend.components import render_downloads, require_analysis
from services.exporter import coloring_dataframe, export_all
from utils.constants import ALGORITHM_LABELS


def render_result_view() -> None:
    """Render coloring results and export controls."""

    st.subheader("Assignment Report")
    analysis = require_analysis()
    if not analysis:
        return

    result = analysis["result"]
    graph = analysis["graph"]
    stats = analysis["stats"]

    columns = st.columns(4)
    columns[0].metric("Strategy", ALGORITHM_LABELS.get(result["algorithm"], result["algorithm"]))
    columns[1].metric("Required categories", result["chromatic_number"])
    columns[2].metric("Execution time", f"{result['execution_time']:.6f}s")
    columns[3].metric("Conflict-free", "Yes" if result["is_valid"] else "No")

    st.dataframe(coloring_dataframe(result["coloring"]), use_container_width=True)
    if result["errors"]:
        st.error("\n".join(result["errors"]))

    if st.button("Generate Planning Pack", use_container_width=True):
        with st.spinner("Creating CSV, Excel, PDF, and map PNG exports..."):
            paths = export_all(graph, result, stats, settings.outputs_dir)
            st.session_state["exports"] = paths
        st.success("Planning pack generated.")

    paths = st.session_state.get("exports")
    if paths:
        render_downloads(paths)
