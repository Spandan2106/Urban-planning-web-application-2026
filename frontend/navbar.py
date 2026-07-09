"""Top navigation/header component."""

from __future__ import annotations

import streamlit as st

from utils.constants import APP_NAME


def render_navbar() -> None:
    """Render the page header."""

    st.markdown(
        f"""
        <div class="planner-hero">
            <div class="planner-kicker">Urban Planning Operations</div>
            <h1 class="planner-title">{APP_NAME}</h1>
            <div class="planner-copy">
                Turn neighborhood adjacency files into clean administrative-zone
                assignments. Inspect boundary pressure, compare allocation
                strategies, and export planning-ready reports.
            </div>
            <div class="planner-strip">
                <div class="planner-tile">
                    <strong>Boundary-aware</strong>
                    <span>Neighboring regions are checked before assignments are approved.</span>
                </div>
                <div class="planner-tile">
                    <strong>Planner-friendly</strong>
                    <span>Upload simple TXT region files and review visual district maps.</span>
                </div>
                <div class="planner-tile">
                    <strong>Report-ready</strong>
                    <span>Export CSV, Excel, PDF, and PNG outputs for meetings.</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
