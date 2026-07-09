"""Custom Streamlit styling."""

from __future__ import annotations

import streamlit as st


def apply_styles() -> None:
    """Apply custom CSS for a clean planning-dashboard interface."""

    st.markdown(
        """
        <style>
        :root {
            --ink: #1f2937;
            --muted: #526070;
            --line: #d7dee8;
            --panel: #ffffff;
            --paper: #f7f9fc;
            --teal: #0f766e;
            --blue: #2563eb;
            --amber: #b7791f;
            --rose: #be3144;
        }
        .stApp {
            background:
                radial-gradient(circle at 14% 12%, rgba(15, 118, 110, 0.13), transparent 24rem),
                radial-gradient(circle at 88% 4%, rgba(37, 99, 235, 0.12), transparent 26rem),
                linear-gradient(180deg, #f4f8fb 0%, #eef4f8 45%, #f8fafc 100%);
            color: var(--ink) !important;
        }
        .main .block-container {
            padding-top: 1.15rem;
            padding-bottom: 2.5rem;
            max-width: 1220px;
        }
        h1, h2, h3, h4, h5, h6 {
            letter-spacing: 0;
            color: var(--ink) !important;
        }
        p, li, label, span, div {
            color: inherit;
        }
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f2435 0%, #183b56 100%);
            border-right: 1px solid rgba(255,255,255,0.12);
        }
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
            color: #f8fafc !important;
        }
        section[data-testid="stSidebar"] [role="radiogroup"] label p,
        section[data-testid="stSidebar"] [data-testid="stMetricLabel"],
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] [data-testid="stMetricValue"] {
            color: #f8fafc !important;
        }
        section[data-testid="stSidebar"] div[data-testid="stMetric"] {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 8px;
            padding: 0.65rem;
        }
        section[data-testid="stSidebar"] [data-baseweb="select"] {
            background: #ffffff !important;
            border: 1px solid rgba(255,255,255,0.45) !important;
        }
        section[data-testid="stSidebar"] [data-baseweb="select"] * {
            color: #1f2937 !important;
        }
        section[data-testid="stSidebar"] svg {
            color: #f8fafc !important;
            fill: currentColor !important;
        }
        section[data-testid="stSidebar"] [data-baseweb="select"] svg {
            color: #1f2937 !important;
        }
        .planner-hero {
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(16, 42, 67, 0.12);
            border-radius: 8px;
            padding: 1.35rem 1.45rem;
            background:
                linear-gradient(135deg, rgba(255,255,255,0.94), rgba(232, 244, 241, 0.9)),
                repeating-linear-gradient(90deg, rgba(15,118,110,0.08) 0 1px, transparent 1px 48px),
                repeating-linear-gradient(0deg, rgba(37,99,235,0.07) 0 1px, transparent 1px 48px);
            box-shadow: 0 18px 50px rgba(16, 42, 67, 0.10);
            margin-bottom: 1.1rem;
        }
        .planner-hero:after {
            content: "";
            position: absolute;
            right: 1.5rem;
            top: 1.15rem;
            width: 12rem;
            height: 12rem;
            background:
                linear-gradient(45deg, transparent 44%, rgba(15,118,110,0.22) 45% 55%, transparent 56%),
                linear-gradient(-45deg, transparent 44%, rgba(37,99,235,0.18) 45% 55%, transparent 56%);
            opacity: 0.8;
            transform: rotate(8deg);
            pointer-events: none;
        }
        .planner-kicker {
            color: #0f766e !important;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.35rem;
        }
        .planner-title {
            max-width: 760px;
            font-size: clamp(2rem, 4vw, 3.6rem);
            line-height: 1.02;
            font-weight: 850;
            color: #102a43 !important;
            margin: 0;
        }
        .planner-copy {
            max-width: 760px;
            color: #40566f !important;
            font-size: 1.05rem;
            line-height: 1.65;
            margin-top: 0.8rem;
        }
        .planner-strip {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.75rem;
            margin: 1rem 0 0.25rem;
        }
        .planner-tile {
            border: 1px solid rgba(16, 42, 67, 0.12);
            border-radius: 8px;
            padding: 0.85rem;
            background: rgba(255,255,255,0.74);
            box-shadow: 0 8px 22px rgba(16, 42, 67, 0.06);
        }
        .planner-tile strong {
            display: block;
            color: #102a43 !important;
            font-size: 0.95rem;
            margin-bottom: 0.2rem;
        }
        .planner-tile span {
            color: var(--muted) !important;
            font-size: 0.88rem;
            line-height: 1.35;
        }
        div[data-testid="stMetric"] {
            background: rgba(255,255,255,0.94);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.85rem;
            box-shadow: 0 10px 24px rgba(16, 42, 67, 0.06);
        }
        div[data-testid="stMetric"] * {
            color: #1f2937 !important;
        }
        div[data-testid="stDataFrame"], div[data-testid="stPlotlyChart"] {
            border: 1px solid var(--line);
            border-radius: 8px;
            overflow: hidden;
            background: var(--panel);
            box-shadow: 0 12px 26px rgba(16, 42, 67, 0.06);
        }
        .stButton > button, .stDownloadButton > button {
            border-radius: 8px;
            border: 1px solid rgba(15, 118, 110, 0.35);
            background: linear-gradient(135deg, #0f766e, #2563eb);
            color: #ffffff !important;
            font-weight: 750;
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.18);
            transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
        }
        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-1px);
            filter: brightness(1.03);
            box-shadow: 0 16px 30px rgba(37, 99, 235, 0.24);
        }
        .stButton > button *, .stDownloadButton > button * {
            color: #ffffff !important;
        }
        .stTextArea textarea, .stSelectbox [data-baseweb="select"], .stFileUploader {
            border-radius: 8px;
        }
        .stTextArea textarea,
        .stTextInput input,
        .stNumberInput input {
            background: #ffffff !important;
            color: #1f2937 !important;
            border: 1px solid #cbd5e1 !important;
        }
        .stTextArea textarea::placeholder,
        .stTextInput input::placeholder {
            color: #64748b !important;
        }
        .stSelectbox [data-baseweb="select"] {
            background: #ffffff !important;
        }
        .stSelectbox [data-baseweb="select"] * {
            color: #1f2937 !important;
        }
        [data-baseweb="popover"],
        [data-baseweb="menu"] {
            background: #ffffff !important;
        }
        [data-baseweb="popover"] *,
        [data-baseweb="menu"] * {
            color: #1f2937 !important;
        }
        [data-testid="stFileUploader"] label {
            color: var(--ink) !important;
        }
        [data-testid="stFileUploader"] {
            background: var(--panel);
            border: 1px dashed #94a3b8;
            border-radius: 8px;
            padding: 0.75rem;
        }
        .workflow-band {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: rgba(255,255,255,0.82);
            padding: 1rem;
            margin: 0.75rem 0;
            box-shadow: 0 10px 24px rgba(16, 42, 67, 0.06);
        }
        .section-note {
            color: var(--muted) !important;
            line-height: 1.55;
            margin-top: -0.25rem;
            margin-bottom: 0.75rem;
        }
        section[data-testid="stSidebar"] [data-baseweb="popover"] {
            background: #183b56 !important;
        }
        section[data-testid="stSidebar"] [data-baseweb="popover"] * {
            color: #f8fafc !important;
            background: #183b56 !important;
        }
        .footer {
            color: #526070 !important;
            font-size: 0.85rem;
            padding-top: 2rem;
        }
        @media (max-width: 760px) {
            .planner-strip {
                grid-template-columns: 1fr;
            }
            .planner-hero:after {
                display: none;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
