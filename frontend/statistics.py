"""Statistics dashboard page."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from frontend.components import require_analysis
from services.statistics import database_statistics


def render_statistics() -> None:
    """Render graph and database statistics."""

    st.subheader("Planning Metrics")
    analysis = require_analysis()
    graph_stats = analysis["stats"] if analysis else {}

    if graph_stats:
        columns = st.columns(5)
        for index, (metric, value) in enumerate(graph_stats.items()):
            columns[index % 5].metric(metric.replace("_", " ").title(), value)

        graph = analysis["graph"]
        degree_frame = pd.DataFrame(
            [{"Region": str(node), "Degree": degree} for node, degree in graph.degree()]
        )
        figure = px.bar(
            degree_frame,
            x="Region",
            y="Degree",
            title="Boundary Pressure by Region",
            color="Degree",
            color_continuous_scale=["#0f766e", "#2563eb", "#be3144"],
        )
        st.plotly_chart(figure, use_container_width=True)

    db_stats = database_statistics()
    st.markdown("**Planning Archive Statistics**")
    st.json(db_stats)
