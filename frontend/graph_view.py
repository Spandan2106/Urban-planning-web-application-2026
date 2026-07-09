"""Graph visualization page."""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from frontend.components import require_analysis
from services.visualization import create_graph_figure


def render_graph_view() -> None:
    """Render the graph visualization page."""

    st.subheader("District Map")
    st.markdown(
        '<div class="section-note">Colored regions show the proposed administrative categories; border labels show neighboring relationships.</div>',
        unsafe_allow_html=True,
    )
    analysis = require_analysis()
    if not analysis:
        return

    graph = analysis["graph"]
    coloring = analysis["result"]["coloring"]
    figure = create_graph_figure(graph, coloring)
    st.pyplot(figure, clear_figure=True)
    plt.close(figure)
