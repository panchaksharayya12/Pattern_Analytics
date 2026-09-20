import streamlit as st
import sys
import os
import base64
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Ensure project root and src are in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))
sys.path.insert(0, str(BASE_DIR))

from data_loader import load_data
from preprocessing import add_age_group
from segmentation import add_segments
from analytics import (
    churn_rate,
    churn_by_group,
    geographic_risk_index,
    high_value_analysis
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Pattern Analytics - European Banking Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ASSETS & BASE64 ENCODING
# =========================================================
@st.cache_data
def get_hero_base64():
    candidates = [
        BASE_DIR / "assets" / "hero_europe_night.png",
        Path(r"C:\Users\panch\.gemini\antigravity\brain\7d77b44e-bb95-4d4e-b6dc-ffd739e9d693\.user_uploaded\media_1789846681072.png"),
        Path(r"C:\Users\panch\.gemini\antigravity\brain\7d77b44e-bb95-4d4e-b6dc-ffd739e9d693\.user_uploaded\media_1789883146205.png"),
    ]
    for c in candidates:
        if c.exists():
            try:
                return base64.b64encode(c.read_bytes()).decode("utf-8")
            except Exception:
                pass
    return ""

HERO_B64 = get_hero_base64()

# =========================================================
# LOAD AND ENRICH DATA
# =========================================================
@st.cache_data
def get_data():
    df_raw = load_data()
    df_proc = add_age_group(df_raw)
    df_proc = add_segments(df_proc)
    return df_proc

df = get_data()

# =========================================================
# DARK CINEMATIC THEME STYLES
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;1,400;1,600&display=swap');

html {
    scroll-behavior: smooth;
}

/* Background & Core Fonts */
.stApp {
    background: radial-gradient(circle at 85% 12%, rgba(26, 54, 93, 0.22) 0%, transparent 45%),
                radial-gradient(circle at 10% 35%, rgba(13, 37, 68, 0.18) 0%, transparent 40%),
                #030712 !important;
    color: #f1f5f9;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.block-container {
    max-width: 1480px;
    padding-top: 0.6rem;
    padding-bottom: 5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Hide standard Streamlit header/footer */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
.stDeployButton { display: none; }

/* Sticky Sub-Navigation Bar */
.sticky-subnav {
    position: -webkit-sticky;
    position: sticky;
    top: 14px;
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 10px 18px;
    margin: 12px auto 28px auto;
    max-width: 860px;
    background: rgba(8, 14, 28, 0.88);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 9999px;
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45);
}

.subnav-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 18px;
    color: #94a3b8 !important;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    border-radius: 9999px;
    transition: all 0.25s ease;
}

.subnav-pill:hover {
    color: #ffffff !important;
    background: rgba(255, 255, 255, 0.10);
    transform: translateY(-1px);
}

/* Master Hero Image Container & Hotspot Links */
.master-hero-container {
    position: relative;
    width: 100%;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.10);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.65);
    margin-bottom: 24px;
    background: #040814;
}

.master-hero-image {
    width: 100%;
    height: auto;
    display: block;
}

/* 5 Clickable Hotspots mapped directly over the painted buttons in the image */
.hero-hotspots-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 15%; /* Corresponds to the top navigation stripe */
    display: grid;
    grid-template-columns: 24% 15% 15% 16% 15% 15%;
    z-index: 10;
}

.hotspot-item {
    display: block;
    width: 100%;
    height: 100%;
    text-decoration: none !important;
    cursor: pointer;
    transition: background 0.2s ease;
}

.hotspot-item:hover {
    background: rgba(255, 255, 255, 0.07);
}

/* Glassmorphic Metric Cards */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin: 20px 0 35px 0;
}

@media (max-width: 992px) {
    .kpi-row { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
    .kpi-row { grid-template-columns: 1fr; }
}

.kpi-card {
    position: relative;
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(9, 14, 26, 0.85) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 22px 24px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    transition: transform 0.25s ease, border-color 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    border-color: rgba(255, 255, 255, 0.22);
}

.kpi-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 20px;
    right: 20px;
    height: 2px;
    border-radius: 2px;
}

.kpi-card.cyan::before { background: linear-gradient(90deg, #38bdf8, transparent); }
.kpi-card.red::before { background: linear-gradient(90deg, #f43f5e, transparent); }
.kpi-card.amber::before { background: linear-gradient(90deg, #f59e0b, transparent); }
.kpi-card.purple::before { background: linear-gradient(90deg, #a855f7, transparent); }

.kpi-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 10px;
}

.kpi-value {
    font-size: 32px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.5px;
    line-height: 1.1;
}

.kpi-sub {
    font-size: 12px;
    color: #64748b;
    margin-top: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Section Dividers & Headers */
.section-anchor {
    padding-top: 30px;
    margin-top: 20px;
}

.section-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.badge-landscape { background: rgba(14, 165, 233, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
.badge-patterns { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.3); }
.badge-finance { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }
.badge-stories { background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(251, 113, 133, 0.3); }

.section-headline {
    font-size: 26px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.5px;
    margin-bottom: 4px;
}

.section-desc {
    font-size: 14px;
    color: #94a3b8;
    max-width: 900px;
    line-height: 1.6;
    margin-bottom: 22px;
}

/* Chart Container Cards */
div[data-testid="stPlotlyChart"] {
    background: rgba(15, 23, 42, 0.65) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    padding: 8px !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
}

/* Sidebar Custom Styling */
section[data-testid="stSidebar"] {
    background: #060b17 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Insight Cards */
.insight-box {
    background: linear-gradient(145deg, rgba(17, 24, 39, 0.8), rgba(9, 14, 26, 0.9));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 20px;
    min-height: 140px;
}

.insight-pill {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #38bdf8;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.insight-lead {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
}

.insight-body {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.5;
    margin-top: 6px;
}

/* Footer */
.master-footer {
    margin-top: 60px;
    padding: 40px 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    text-align: center;
    background: #02050c;
    border-radius: 14px;
}

.master-footer strong {
    font-size: 16px;
    letter-spacing: 1.5px;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# MASTER HERO BANNER WITH DIRECT REFERENCE IMAGE & HOTSPOTS
# =========================================================
if HERO_B64:
    st.markdown(f"""
    <div class="master-hero-container">
        <img src="data:image/png;base64,{HERO_B64}" class="master-hero-image" alt="Pattern Analytics - European Banking Intelligence" />
        <div class="hero-hotspots-bar">
            <a href="#overview" class="hotspot-item" title="Pattern Analytics Home"></a>
            <a href="#overview" class="hotspot-item" title="Overview Section"></a>
            <a href="#landscape" class="hotspot-item" title="Landscape Section"></a>
            <a href="#patterns" class="hotspot-item" title="Customer Patterns Section"></a>
            <a href="#financial-risk" class="hotspot-item" title="Financial Risk Section"></a>
            <a href="#customer-stories" class="hotspot-item" title="Customer Stories Section"></a>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Fallback banner if image is not present
    st.markdown("""
    <div style="background: linear-gradient(135deg, #070d1e 0%, #03060f 100%); padding: 50px 40px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 25px;">
        <div style="font-size: 11px; font-weight: 800; letter-spacing: 2px; color: #38bdf8; text-transform: uppercase;">European Banking - Customer Intelligence</div>
        <h1 style="font-size: 52px; font-weight: 800; color: #ffffff; margin: 10px 0;">Understanding <span style="font-family: 'Playfair Display', serif; font-style: italic; color: #7dd3fc;">why customers leave.</span></h1>
        <p style="font-size: 16px; color: #94a3b8; max-width: 700px; line-height: 1.6;">Pattern Analytics explores customer segmentation, churn behavior, geographic differences, engagement signals and high-value customer exposure across a 10,000-customer European banking dataset.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# STICKY FLOATING SUBNAV
# =========================================================
st.markdown("""
<div class="sticky-subnav">
    <a href="#overview" class="subnav-pill">Overview</a>
    <a href="#landscape" class="subnav-pill">Landscape</a>
    <a href="#patterns" class="subnav-pill">Customer Patterns</a>
    <a href="#financial-risk" class="subnav-pill">Financial Risk</a>
    <a href="#customer-stories" class="subnav-pill">Customer Stories</a>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR CONTROLS
# =========================================================
st.sidebar.markdown("""
<div style="padding: 10px 0 16px 0; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 18px;">
    <div style="font-size: 11px; font-weight: 800; letter-spacing: 2px; color: #38bdf8; text-transform: uppercase;">PORTFOLIO CONTROLS</div>
    <div style="font-size: 16px; font-weight: 700; color: #ffffff; margin-top: 4px;">Dynamic Filters</div>
</div>
""", unsafe_allow_html=True)

geographies = st.sidebar.multiselect(
    "Geography (Market)",
    options=sorted(df["Geography"].unique()),
    default=sorted(df["Geography"].unique())
)

genders = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["Gender"].unique()),
    default=sorted(df["Gender"].unique())
)

activity = st.sidebar.selectbox(
    "Member Activity Status",
    options=["All Accounts", "Active Members Only", "Inactive Members Only"]
)

# Apply Filtered Dataset
filtered_df = df[
    df["Geography"].isin(geographies) &
    df["Gender"].isin(genders)
].copy()

if activity == "Active Members Only":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 1]
elif activity == "Inactive Members Only":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 0]

st.sidebar.markdown("---")
st.sidebar.caption(
    f"Filtered Sample: **{len(filtered_df):,}** of **{len(df):,}** records ({len(filtered_df)/len(df)*100:.1f}%)"
)

# Helper function for Plotly Dark Theme
def apply_plotly_dark(fig, title_text="", x_title="", y_title=""):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(15, 23, 42, 0.4)",
        plot_bgcolor="rgba(15, 23, 42, 0.4)",
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#94a3b8", size=11),
        title=dict(
            text=title_text,
            font=dict(size=14, color="#f8fafc", family="Plus Jakarta Sans, sans-serif", weight="bold")
        ),
        margin=dict(l=35, r=25, t=55, b=40),
        xaxis=dict(
            title=x_title,
            gridcolor="rgba(255, 255, 255, 0.05)",
            zerolinecolor="rgba(255, 255, 255, 0.08)",
            tickfont=dict(color="#cbd5e1")
        ),
        yaxis=dict(
            title=y_title,
            gridcolor="rgba(255, 255, 255, 0.05)",
            zerolinecolor="rgba(255, 255, 255, 0.08)",
            tickfont=dict(color="#cbd5e1")
        ),
        legend=dict(
            bgcolor="rgba(15, 23, 42, 0.8)",
            bordercolor="rgba(255, 255, 255, 0.08)",
            borderwidth=1,
            font=dict(color="#e2e8f0")
        )
    )
    return fig

# =========================================================
# SECTION 1: OVERVIEW & EXECUTIVE METRICS
# =========================================================
st.markdown('<div id="overview" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-badge badge-landscape">01 - EXECUTIVE SUMMARY</div>
<div class="section-headline">Retail Banking Portfolio Overview</div>
<div class="section-desc">Key performance indicators, observed customer churn, and balance exposure metrics across European consumer accounts.</div>
""", unsafe_allow_html=True)

total_customers = len(filtered_df)
total_churned = int(filtered_df["Exited"].sum()) if total_customers > 0 else 0
filtered_churn_rate = churn_rate(filtered_df) if total_customers > 0 else 0.0

high_val_df = filtered_df[filtered_df["HighValue"]]
high_val_count = len(high_val_df)
high_val_churned = int(high_val_df["Exited"].sum()) if high_val_count > 0 else 0
high_val_churn_rate = churn_rate(high_val_df) if high_val_count > 0 else 0.0

total_churn_balance_exposure = filtered_df.loc[filtered_df["Exited"] == 1, "Balance"].sum() if total_customers > 0 else 0.0

st.markdown(f"""
<div class="kpi-row">
    <div class="kpi-card cyan">
        <div class="kpi-label">TOTAL PORTFOLIO</div>
        <div class="kpi-value">{total_customers:,}</div>
        <div class="kpi-sub">Analyzed Customer Accounts</div>
    </div>
    <div class="kpi-card red">
        <div class="kpi-label">OBSERVED CHURN RATE</div>
        <div class="kpi-value">{filtered_churn_rate:.2f}%</div>
        <div class="kpi-sub">{total_churned:,} Total Churned Accounts</div>
    </div>
    <div class="kpi-card amber">
        <div class="kpi-label">HIGH-VALUE CHURN</div>
        <div class="kpi-value">{high_val_churn_rate:.2f}%</div>
        <div class="kpi-sub">{high_val_churned:,} of {high_val_count:,} High-Value Accounts</div>
    </div>
    <div class="kpi-card purple">
        <div class="kpi-label">BALANCE EXPOSURE</div>
        <div class="kpi-value">&euro;{total_churn_balance_exposure/1e6:,.1f}M</div>
        <div class="kpi-sub">Total Capital at Flight Risk</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SECTION 2: LANDSCAPE - GEOGRAPHIC & DEMOGRAPHIC
# =========================================================
st.markdown('<div id="landscape" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-badge badge-landscape">02 - THE LANDSCAPE</div>
<div class="section-headline">Geographic Variance & Demographic Gradients</div>
<div class="section-desc">Cross-market churn patterns between Germany, France, and Spain, coupled with age and tenure segmentation.</div>
""", unsafe_allow_html=True)

if total_customers > 0:
    geo_df = geographic_risk_index(filtered_df).reset_index()

    geo_col1, geo_col2 = st.columns(2)

    with geo_col1:
        fig_geo = px.bar(
            geo_df,
            x="Geography",
            y="Churn_Rate",
            text="Churn_Rate",
            color="Geography",
            color_discrete_map={"Germany": "#f43f5e", "Spain": "#38bdf8", "France": "#818cf8"},
            title="Observed Churn Rate by Country (%)"
        )
        fig_geo.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_geo = apply_plotly_dark(fig_geo, "Observed Churn Rate by Country", "Geography", "Churn Rate (%)")
        fig_geo.update_layout(showlegend=False)
        st.plotly_chart(fig_geo, use_container_width=True)

    with geo_col2:
        fig_risk = px.bar(
            geo_df,
            x="Geography",
            y="Risk_Index",
            text="Risk_Index",
            color="Geography",
            color_discrete_map={"Germany": "#f59e0b", "Spain": "#38bdf8", "France": "#818cf8"},
            title="Geographic Risk Index (Baseline = 1.00)"
        )
        fig_risk.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig_risk = apply_plotly_dark(fig_risk, "Geographic Risk Index (Relative to Average)", "Geography", "Risk Ratio")
        fig_risk.update_layout(showlegend=False)
        st.plotly_chart(fig_risk, use_container_width=True)

    # Demographic Analysis: Age and Tenure
    demo_col1, demo_col2 = st.columns(2)

    with demo_col1:
        age_df = churn_by_group(filtered_df, "AgeGroup").reset_index()
        age_order = ["Under 30", "30-45", "46-60", "60+"]
        age_df["AgeGroup"] = pd.Categorical(age_df["AgeGroup"], categories=age_order, ordered=True)
        age_df = age_df.sort_values("AgeGroup")

        fig_age = px.bar(
            age_df,
            x="AgeGroup",
            y="Churn_Rate",
            text="Churn_Rate",
            color="Churn_Rate",
            color_continuous_scale="Reds",
            title="Observed Churn Rate by Age Segment"
        )
        fig_age.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_age = apply_plotly_dark(fig_age, "Churn Rate by Age Segment (%)", "Age Group", "Churn Rate (%)")
        fig_age.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_age, use_container_width=True)

    with demo_col2:
        tenure_df = churn_by_group(filtered_df, "TenureGroup").reset_index()
        tenure_order = ["New", "Mid-term", "Long-term"]
        tenure_df["TenureGroup"] = pd.Categorical(tenure_df["TenureGroup"], categories=tenure_order, ordered=True)
        tenure_df = tenure_df.sort_values("TenureGroup")

        fig_tenure = px.bar(
            tenure_df,
            x="TenureGroup",
            y="Churn_Rate",
            text="Churn_Rate",
            color_discrete_sequence=["#38bdf8"],
            title="Observed Churn Rate by Customer Tenure Group"
        )
        fig_tenure.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_tenure = apply_plotly_dark(fig_tenure, "Churn Rate by Customer Tenure", "Tenure Category", "Churn Rate (%)")
        st.plotly_chart(fig_tenure, use_container_width=True)

    # Geographic x Age Group Interaction
    st.markdown("#### Geographic &times; Age Group Interaction")
    geo_age_raw = filtered_df.groupby(["Geography", "AgeGroup"], observed=False)["Exited"].mean().reset_index()
    geo_age_raw["Churn_Rate"] = (geo_age_raw["Exited"] * 100).round(2)
    geo_age_raw["AgeGroup"] = pd.Categorical(geo_age_raw["AgeGroup"], categories=age_order, ordered=True)
    geo_age_raw = geo_age_raw.sort_values(["Geography", "AgeGroup"])

    fig_geo_age = px.bar(
        geo_age_raw,
        x="Geography",
        y="Churn_Rate",
        color="AgeGroup",
        barmode="group",
        text="Churn_Rate",
        color_discrete_sequence=["#38bdf8", "#818cf8", "#f43f5e", "#fbbf24"],
        title="Cross-Market Age Churn Dynamics"
    )
    fig_geo_age.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig_geo_age = apply_plotly_dark(fig_geo_age, "Cross-Market Age Segment Churn (%)", "Geography", "Churn Rate (%)")
    st.plotly_chart(fig_geo_age, use_container_width=True)

# =========================================================
# SECTION 3: CUSTOMER PATTERNS - BEHAVIORAL SIGNALS
# =========================================================
st.markdown('<div id="patterns" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-badge badge-patterns">03 - CUSTOMER PATTERNS</div>
<div class="section-headline">Behavioral Signals & Product Friction</div>
<div class="section-desc">Analyzing the influence of product bundling, credit score tiers, and digital engagement on customer retention.</div>
""", unsafe_allow_html=True)

if total_customers > 0:
    pat_col1, pat_col2 = st.columns(2)

    with pat_col1:
        prod_df = churn_by_group(filtered_df, "NumOfProducts").reset_index()
        prod_df["NumOfProducts"] = prod_df["NumOfProducts"].astype(str) + " Product(s)"

        fig_prod = px.bar(
            prod_df,
            x="NumOfProducts",
            y="Churn_Rate",
            text="Churn_Rate",
            color="Churn_Rate",
            color_continuous_scale="Viridis",
            title="Churn Rate by Number of Products Held"
        )
        fig_prod.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_prod = apply_plotly_dark(fig_prod, "Product Bundling vs Churn Rate (%)", "Number of Products", "Churn Rate (%)")
        fig_prod.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_prod, use_container_width=True)

    with pat_col2:
        cred_df = churn_by_group(filtered_df, "CreditScoreGroup").reset_index()
        cred_order = ["Low", "Medium", "High"]
        cred_df["CreditScoreGroup"] = pd.Categorical(cred_df["CreditScoreGroup"], categories=cred_order, ordered=True)
        cred_df = cred_df.sort_values("CreditScoreGroup")

        fig_cred = px.bar(
            cred_df,
            x="CreditScoreGroup",
            y="Churn_Rate",
            text="Churn_Rate",
            color_discrete_sequence=["#a855f7"],
            title="Observed Churn Rate by Credit Score Group"
        )
        fig_cred.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_cred = apply_plotly_dark(fig_cred, "Credit Score Tier vs Churn Rate (%)", "Credit Score Tier", "Churn Rate (%)")
        st.plotly_chart(fig_cred, use_container_width=True)

    # Activity & Gender Behavioral Breakdown
    act_col1, act_col2 = st.columns(2)

    with act_col1:
        act_df = churn_by_group(filtered_df, "IsActiveMember").reset_index()
        act_df["Activity"] = act_df["IsActiveMember"].map({0: "Inactive Member", 1: "Active Member"})

        fig_act = px.bar(
            act_df,
            x="Activity",
            y="Churn_Rate",
            text="Churn_Rate",
            color="Activity",
            color_discrete_map={"Inactive Member": "#f43f5e", "Active Member": "#10b981"},
            title="Active vs Inactive Customer Churn Rate"
        )
        fig_act.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_act = apply_plotly_dark(fig_act, "Engagement Level Impact on Churn", "Engagement Status", "Churn Rate (%)")
        fig_act.update_layout(showlegend=False)
        st.plotly_chart(fig_act, use_container_width=True)

    with act_col2:
        gen_df = churn_by_group(filtered_df, "Gender").reset_index()
        fig_gen = px.bar(
            gen_df,
            x="Gender",
            y="Churn_Rate",
            text="Churn_Rate",
            color="Gender",
            color_discrete_map={"Female": "#ec4899", "Male": "#38bdf8"},
            title="Observed Churn Rate by Gender"
        )
        fig_gen.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_gen = apply_plotly_dark(fig_gen, "Gender Disparity in Churn Rate", "Gender", "Churn Rate (%)")
        fig_gen.update_layout(showlegend=False)
        st.plotly_chart(fig_gen, use_container_width=True)

# =========================================================
# SECTION 4: FINANCIAL RISK & BALANCE EXPOSURE
# =========================================================
st.markdown('<div id="financial-risk" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-badge badge-finance">04 - FINANCIAL RISK</div>
<div class="section-headline">Balance Concentration & Capital Flight Exposure</div>
<div class="section-desc">Quantifying capital flight across balance bands, estimated compensation tiers, and high-value customer accounts.</div>
""", unsafe_allow_html=True)

if total_customers > 0:
    fin_col1, fin_col2 = st.columns(2)

    with fin_col1:
        bal_df = churn_by_group(filtered_df, "BalanceGroup").reset_index()
        bal_order = ["Zero Balance", "Low Balance", "High Balance"]
        bal_df["BalanceGroup"] = pd.Categorical(bal_df["BalanceGroup"], categories=bal_order, ordered=True)
        bal_df = bal_df.sort_values("BalanceGroup")

        fig_bal = px.bar(
            bal_df,
            x="BalanceGroup",
            y="Churn_Rate",
            text="Churn_Rate",
            color_discrete_sequence=["#fbbf24"],
            title="Observed Churn Rate by Balance Segment"
        )
        fig_bal.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_bal = apply_plotly_dark(fig_bal, "Account Balance Tier vs Churn (%)", "Balance Tier", "Churn Rate (%)")
        st.plotly_chart(fig_bal, use_container_width=True)

    with fin_col2:
        scatter_sample = filtered_df.sample(min(1200, len(filtered_df)), random_state=42).copy()
        scatter_sample["Status"] = scatter_sample["Exited"].map({0: "Retained", 1: "Churned"})

        fig_scat = px.scatter(
            scatter_sample,
            x="EstimatedSalary",
            y="Balance",
            color="Status",
            color_discrete_map={"Retained": "#0ea5e9", "Churned": "#f43f5e"},
            opacity=0.65,
            hover_data=["CustomerId", "Geography", "Age", "CreditScore"],
            title="Estimated Salary vs Account Balance (Sampled)"
        )
        fig_scat = apply_plotly_dark(fig_scat, "Salary vs Account Balance Distribution", "Estimated Salary (\u20ac)", "Account Balance (\u20ac)")
        st.plotly_chart(fig_scat, use_container_width=True)

    # Balance Exposure Metrics
    avg_bal_churned = filtered_df.loc[filtered_df["Exited"] == 1, "Balance"].mean() if total_churned > 0 else 0.0
    avg_bal_retained = filtered_df.loc[filtered_df["Exited"] == 0, "Balance"].mean() if (total_customers - total_churned) > 0 else 0.0
    hv_exposure = high_val_df.loc[high_val_df["Exited"] == 1, "Balance"].sum() if high_val_count > 0 else 0.0

    st.markdown(f"""
    <div class="kpi-row">
        <div class="kpi-card red">
            <div class="kpi-label">AVG BALANCE - CHURNED</div>
            <div class="kpi-value">&euro;{avg_bal_churned:,.0f}</div>
            <div class="kpi-sub">+{((avg_bal_churned/avg_bal_retained)-1)*100:.1f}% vs Retained Average</div>
        </div>
        <div class="kpi-card cyan">
            <div class="kpi-label">AVG BALANCE - RETAINED</div>
            <div class="kpi-value">&euro;{avg_bal_retained:,.0f}</div>
            <div class="kpi-sub">Stable Account Baseline</div>
        </div>
        <div class="kpi-card amber">
            <div class="kpi-label">HIGH-VALUE EXPOSURE</div>
            <div class="kpi-value">&euro;{hv_exposure/1e6:,.1f}M</div>
            <div class="kpi-sub">{(hv_exposure / total_churn_balance_exposure * 100) if total_churn_balance_exposure > 0 else 0:.1f}% of Total Capital Exposure</div>
        </div>
        <div class="kpi-card purple">
            <div class="kpi-label">TOTAL BALANCE AT RISK</div>
            <div class="kpi-value">&euro;{total_churn_balance_exposure:,.0f}</div>
            <div class="kpi-sub">Cumulative Churned Capital</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SECTION 5: CUSTOMER STORIES - INDIVIDUAL DRILL-DOWN
# =========================================================
st.markdown('<div id="customer-stories" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-badge badge-stories">05 - CUSTOMER STORIES</div>
<div class="section-headline">Individual Account Explorer & Drill-Down</div>
<div class="section-desc">Search, filter, inspect granular account profiles, and export individual customer cohorts for targeted retention interventions.</div>
""", unsafe_allow_html=True)

exp_col1, exp_col2 = st.columns([1, 2])

with exp_col1:
    explorer_view = st.selectbox(
        "Filter Account Segment",
        ["All Accounts", "Churned Accounts Only", "High-Value Accounts", "High-Value Churners Only"]
    )

with exp_col2:
    search_query = st.text_input(
        "Search Customer ID or Surname",
        placeholder="Search e.g. 15634602, Hargrave, Mitchell..."
    )

exp_df = filtered_df.copy()

if explorer_view == "Churned Accounts Only":
    exp_df = exp_df[exp_df["Exited"] == 1]
elif explorer_view == "High-Value Accounts":
    exp_df = exp_df[exp_df["HighValue"] == True]
elif explorer_view == "High-Value Churners Only":
    exp_df = exp_df[(exp_df["HighValue"] == True) & (exp_df["Exited"] == 1)]

if search_query:
    q = search_query.strip().lower()
    exp_df = exp_df[
        exp_df["CustomerId"].astype(str).str.contains(q, na=False) |
        exp_df["Surname"].astype(str).str.lower().str.contains(q, na=False)
    ]

# Display columns
display_cols = [
    "CustomerId", "Surname", "Geography", "Gender", "Age", "CreditScore",
    "Tenure", "Balance", "EstimatedSalary", "NumOfProducts", "IsActiveMember", "HighValue", "Exited"
]
table_df = exp_df[display_cols].copy()
table_df["Status"] = table_df["Exited"].map({0: "Retained", 1: "Churned"})
table_df["HighValue"] = table_df["HighValue"].map({True: "Yes", False: "No"})
table_df["Active"] = table_df["IsActiveMember"].map({1: "Active", 0: "Inactive"})
table_df["Balance (\u20ac)"] = table_df["Balance"].apply(lambda x: f"\u20ac{x:,.2f}")
table_df["Salary (\u20ac)"] = table_df["EstimatedSalary"].apply(lambda x: f"\u20ac{x:,.2f}")

show_df = table_df[[
    "CustomerId", "Surname", "Geography", "Gender", "Age", "CreditScore",
    "Tenure", "Balance (\u20ac)", "Salary (\u20ac)", "NumOfProducts", "Active", "HighValue", "Status"
]]

st.markdown(f"**Showing {len(show_df):,} matching customer accounts**")
st.dataframe(show_df, use_container_width=True, hide_index=True)

# CSV Export
csv_export = exp_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Customer Cohort as CSV",
    data=csv_export,
    file_name="pattern_analytics_customer_cohort.csv",
    mime="text/csv"
)

# Dynamic Executive Insights
st.markdown("---")
st.markdown("### Executive Synthesis & Retention Priorities")

if total_customers > 0:
    highest_age_cat = age_df.loc[age_df["Churn_Rate"].idxmax(), "AgeGroup"]
    highest_age_val = age_df["Churn_Rate"].max()
    highest_geo_cat = geo_df.loc[geo_df["Churn_Rate"].idxmax(), "Geography"]
    highest_geo_val = geo_df["Churn_Rate"].max()
    
    act_inactive_rate = act_df.loc[act_df["IsActiveMember"] == 0, "Churn_Rate"].values[0] if 0 in act_df["IsActiveMember"].values else 0
    act_active_rate = act_df.loc[act_df["IsActiveMember"] == 1, "Churn_Rate"].values[0] if 1 in act_df["IsActiveMember"].values else 0

    ins_col1, ins_col2, ins_col3 = st.columns(3)

    with ins_col1:
        st.markdown(f"""
        <div class="insight-box">
            <div class="insight-pill">CRITICAL AGE HAZARD</div>
            <div class="insight-lead">{highest_age_cat}</div>
            <div class="insight-body">
                Accounts in this demographic show a peak churn rate of <strong>{highest_age_val:.2f}%</strong>, representing the highest concentration of attrition across the entire institution.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with ins_col2:
        st.markdown(f"""
        <div class="insight-box">
            <div class="insight-pill">REGIONAL CAPITAL FLIGHT</div>
            <div class="insight-lead">{highest_geo_cat} ({highest_geo_val:.2f}%)</div>
            <div class="insight-body">
                The German subsidiary exhibits severe churn elevation (Risk Index: <strong>{geo_df.loc[geo_df['Geography']=='Germany', 'Risk_Index'].values[0]:.2f}</strong>), demanding localized fee structure re-evaluations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with ins_col3:
        st.markdown(f"""
        <div class="insight-box">
            <div class="insight-pill">ENGAGEMENT MULTIPLIER</div>
            <div class="insight-lead">Inactive: {act_inactive_rate:.2f}% vs Active: {act_active_rate:.2f}%</div>
            <div class="insight-body">
                Disengaged customer accounts exhibit an 88% surge in attrition probability. Early inactivity triggers provide a critical window for automated re-engagement.
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="master-footer">
    <strong>PATTERN ANALYTICS - EUROPEAN BANKING CUSTOMER INTELLIGENCE</strong><br>
    <div style="color: #64748b; font-size: 13px; margin-top: 8px;">
        Descriptive empirical segmentation on 10,000 retail banking accounts across France, Germany, and Spain.<br>
        All observed metrics reflect empirical patterns; metrics should be interpreted as risk associations rather than deterministic causal relations.
    </div>
</div>
""", unsafe_allow_html=True)
