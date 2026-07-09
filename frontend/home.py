"""Home page."""

from __future__ import annotations

import streamlit as st


def render_home() -> None:
    """Render the home page."""

    st.subheader("Planning Workspace")
    st.markdown(
        """
        <div class="section-note">
        This workspace helps planning teams assign service zones, administrative
        categories, or review districts without placing the same category on
        directly neighboring regions.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="workflow-band">
            <strong>Typical workflow:</strong>
            prepare a region adjacency TXT file, choose a planning strategy,
            review the generated district map, validate conflicts, then export
            the assignment pack for documentation.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        **Accepted region-file formats**
        - `A B` for one edge per line
        - `A,B` for comma-separated edges
        - `A: B C D` for adjacency lists
        - `A` for an isolated region
        """
    )
