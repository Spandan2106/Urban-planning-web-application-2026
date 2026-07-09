"""Footer component."""

from __future__ import annotations

import streamlit as st


def render_footer() -> None:
    """Render the footer."""

    st.markdown(
        '<div class="footer">Civic Region Planner - Python, Streamlit, NetworkX, and MongoDB.</div>',
        unsafe_allow_html=True,
    )
