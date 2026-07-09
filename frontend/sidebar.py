"""Sidebar navigation and settings."""

from __future__ import annotations

import streamlit as st

from services.statistics import database_statistics
from utils.constants import ALGORITHMS, ALGORITHM_LABELS


def render_sidebar() -> tuple[str, str]:
    """Render sidebar controls and return the selected page and algorithm."""

    st.sidebar.header("Planner Console")
    page = st.sidebar.radio(
        "Workspace",
        [
            "Overview",
            "Region Data",
            "District Map",
            "Assignment Report",
            "Planning Metrics",
            "Settings",
        ],
    )
    algorithm = st.sidebar.selectbox(
        "Planning strategy",
        ALGORITHMS,
        format_func=lambda value: ALGORITHM_LABELS.get(value, value),
    )
    st.sidebar.divider()
    db_stats = database_statistics()
    st.sidebar.metric("Planning archive", str(db_stats["status"]).title())
    st.sidebar.metric("Saved plans", int(db_stats["results"]))
    return page, algorithm
