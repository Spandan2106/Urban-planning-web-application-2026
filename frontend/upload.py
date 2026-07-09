"""Upload page."""

from __future__ import annotations

import streamlit as st

from config.settings import settings
from routes.api import process_graph_dataset
from utils.file_utils import safe_filename, write_uploaded_file
from utils.logger import get_logger

logger = get_logger(__name__)


def render_upload(algorithm: str) -> None:
    """Render dataset upload and processing controls."""

    st.subheader("Region Data Intake")
    st.markdown(
        '<div class="section-note">Upload a TXT file that lists regions and shared borders.</div>',
        unsafe_allow_html=True,
    )
    uploaded = st.file_uploader("TXT region adjacency file", type=["txt"])
    sample = st.text_area(
        "Or paste region adjacency text",
        value="A: B C\nB: A C D\nC: A B D\nD: B C E\nE: D",
        height=150,
    )

    if st.button("Generate Region Assignment", type="primary", use_container_width=True):
        try:
            if uploaded is not None:
                filename = safe_filename(uploaded.name)
                content_bytes = uploaded.getvalue()
                write_uploaded_file(content_bytes, settings.uploads_dir / filename)
                content = content_bytes.decode("utf-8")
                name = filename
            else:
                content = sample
                name = "pasted_graph.txt"

            with st.spinner("Reading boundaries, assigning categories, and saving the plan..."):
                analysis = process_graph_dataset(name, content, algorithm)
                st.session_state["analysis"] = analysis
            if analysis.get("result", {}).get("timed_out"):
                st.warning(
                    "The optimal coloring search took too long and was stopped. "
                    "A faster, non-optimal result is shown."
                )
            st.success("Region assignment generated successfully.")
            logger.info("Processed graph dataset %s with %s", name, algorithm)
        except Exception as exc:
            logger.exception("Failed to process graph")
            st.error(f"Could not process the region file: {exc}")
