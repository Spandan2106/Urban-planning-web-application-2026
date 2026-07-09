"""Streamlit entry point for the Civic Region Planner."""

from __future__ import annotations

import streamlit as st

from frontend.footer import render_footer
from frontend.graph_view import render_graph_view
from frontend.home import render_home
from frontend.navbar import render_navbar
from frontend.result_view import render_result_view
from frontend.sidebar import render_sidebar
from frontend.statistics import render_statistics
from frontend.styles import apply_styles
from frontend.upload import render_upload


def render_settings() -> None:
    """Render application settings information."""

    st.subheader("Settings")
    st.write("Configure the planning archive with a local `.env` file using `.env.example` as a template.")
    st.code("MONGODB_URI=mongodb://localhost:27017\nMONGODB_DB=graph_coloring")


def main() -> None:
    """Run the Streamlit application."""

    st.set_page_config(page_title="Civic Region Planner", page_icon="assets/icon.png", layout="wide")
    apply_styles()
    render_navbar()
    page, algorithm = render_sidebar()

    if page == "Overview":
        render_home()
    elif page == "Region Data":
        render_upload(algorithm)
    elif page == "District Map":
        render_graph_view()
    elif page == "Assignment Report":
        render_result_view()
    elif page == "Planning Metrics":
        render_statistics()
    else:
        render_settings()

    render_footer()


if __name__ == "__main__":
    main()
