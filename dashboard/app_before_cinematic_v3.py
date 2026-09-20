import streamlit as st
import sys
import plotly.express as px
import pandas as pd

sys.path.insert(0, "src")

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
    page_title="Pattern Analytics",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# LOAD DATA
# =========================================================

df = load_data()
df = add_age_group(df)


# =========================================================
# PROFESSIONAL DASHBOARD STYLING
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #f6f8fc;
    }

    /* Main content area */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    /* Main title */
    h1 {
        color: #172033;
        font-weight: 800;
        letter-spacing: -1px;
    }

    /* Section headings */
    h2, h3 {
        color: #172033;
        font-weight: 700;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #eef2f7;
        border-right: 1px solid #dce2ea;
    }

    /* KPI cards */
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e2e7ef;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 4px 14px rgba(20, 30, 50, 0.06);
    }

    div[data-testid="stMetricLabel"] {
        color: #667085;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #172033;
        font-weight: 800;
    }

    /* Buttons */
    .stDownloadButton button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Data tables */
    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e2e7ef;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        border: 1px solid #e2e7ef;
        border-radius: 12px;
        background: white;
    }

</style>
""", unsafe_allow_html=True)


df = add_segments(df)


# =========================================================
# CINEMATIC WEBSITE DESIGN
# =========================================================

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #f5f5f2;
}

.block-container {
    max-width: 1500px;
    padding-top: 0.5rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}

header[data-testid="stHeader"] {
    background: transparent;
}


/* ========================================================
   CINEMATIC NAVIGATION
   ======================================================== */

.cinematic-nav {
    position: relative;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 26px;
    margin-bottom: 12px;
    background: #ffffff;
    border-bottom: 1px solid #e5e5e0;
}

.brand {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #111111;
}

.brand span {
    font-weight: 400;
}

.nav-links {
    display: flex;
    gap: 26px;
}

.nav-links a {
    color: #333333 !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
}

.nav-links a:hover {
    color: #c1121f !important;
}


/* ========================================================
   CINEMATIC HERO
   ======================================================== */

.cinematic-hero {
    position: relative;
    min-height: 610px;
    display: flex;
    align-items: flex-end;
    overflow: hidden;
    margin-bottom: 55px;
    background:
        radial-gradient(
            ellipse at 80% 20%,
            rgba(48, 78, 150, 0.65),
            transparent 35%
        ),
        radial-gradient(
            ellipse at 25% 75%,
            rgba(116, 30, 43, 0.45),
            transparent 40%
        ),
        linear-gradient(
            125deg,
            #07090e 0%,
            #111827 45%,
            #182a4d 100%
        );
}

.cinematic-hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(
            115deg,
            transparent 0%,
            rgba(255,255,255,0.035) 35%,
            transparent 36%,
            transparent 55%,
            rgba(255,255,255,0.025) 56%,
            transparent 57%
        );
    opacity: 0.9;
}

.cinematic-hero::after {
    content: "";
    position: absolute;
    width: 620px;
    height: 620px;
    right: -220px;
    top: -230px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow:
        0 0 0 80px rgba(255,255,255,0.025),
        0 0 0 160px rgba(255,255,255,0.018);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 900px;
    padding: 70px 70px 75px 70px;
}

.hero-eyebrow {
    margin-bottom: 22px;
    color: #d8d8d3;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.hero-title {
    margin: 0;
    color: #ffffff;
    font-size: clamp(44px, 6vw, 78px);
    line-height: 0.98;
    font-weight: 800;
    letter-spacing: -3px;
}

.hero-title em {
    color: #d6d6d0;
    font-style: normal;
    font-weight: 400;
}

.hero-description {
    max-width: 690px;
    margin-top: 28px;
    color: rgba(255,255,255,0.74);
    font-size: 17px;
    line-height: 1.65;
}

.hero-line {
    width: 70px;
    height: 3px;
    margin-top: 32px;
    background: #c1121f;
}


/* ========================================================
   SECTION INTRO
   ======================================================== */

.editorial-section {
    padding: 15px 12px 25px 12px;
}

.editorial-kicker {
    color: #c1121f;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.editorial-title {
    margin-top: 7px;
    color: #111111;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
}

.editorial-description {
    max-width: 800px;
    color: #666666;
    font-size: 15px;
    line-height: 1.6;
}


/* ========================================================
   KPI CARDS
   ======================================================== */

div[data-testid="stMetric"] {
    min-height: 125px;
    padding: 22px;
    background: #ffffff;
    border: 0;
    border-radius: 0;
    border-top: 3px solid #111111;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #666666;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

div[data-testid="stMetricValue"] {
    color: #111111;
    font-size: 32px;
    font-weight: 800;
}


/* ========================================================
   SIDEBAR
   ======================================================== */

section[data-testid="stSidebar"] {
    background: #111111;
}

section[data-testid="stSidebar"] * {
    color: #eeeeee !important;
}

section[data-testid="stSidebar"] label {
    font-weight: 600;
}


/* ========================================================
   CHARTS
   ======================================================== */

div[data-testid="stPlotlyChart"] {
    padding: 4px;
    background: #ffffff;
    box-shadow: 0 7px 24px rgba(0,0,0,0.045);
}


/* ========================================================
   TABLES
   ======================================================== */

div[data-testid="stDataFrame"] {
    border-radius: 0;
    border: 1px solid #deded8;
}


/* ========================================================
   FOOTER
   ======================================================== */

.cinematic-footer {
    margin-top: 80px;
    padding: 45px 30px;
    background: #111111;
    color: #aaaaaa;
    text-align: center;
}

.cinematic-footer strong {
    color: #ffffff;
    font-size: 18px;
}

.cinematic-footer .red {
    color: #c1121f;
}


@media (max-width: 800px) {

    .cinematic-nav {
        padding: 15px;
    }

    .nav-links {
        display: none;
    }

    .cinematic-hero {
        min-height: 520px;
    }

    .hero-content {
        padding: 45px 28px;
    }

    .hero-title {
        font-size: 46px;
        letter-spacing: -2px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# CINEMATIC NAVIGATION
# =========================================================

st.html("""
<div class="cinematic-nav">

    <div class="brand">
        PATTERN <span>ANALYTICS</span>
    </div>

    <div class="nav-links">
        <a href="#executive-summary">Overview</a>
        <a href="#geographic-churn-analysis">Geography</a>
        <a href="#product-credit-score-analysis">Segments</a>
        <a href="#financial-geographic-deep-dive">Financial Risk</a>
        <a href="#customer-drill-down-high-value-explorer">Customers</a>
    </div>

</div>
""")


# =========================================================
# CINEMATIC HERO
# =========================================================

st.html("""
<div class="cinematic-hero">

    <div class="hero-content">

        <div class="hero-eyebrow">
            European Banking · Customer Intelligence
        </div>

        <div class="hero-title">
            Understanding<br>
            <em>why customers leave.</em>
        </div>

        <div class="hero-description">
            Pattern Analytics explores customer segmentation, churn
            behavior, geographic differences, engagement signals and
            high-value customer exposure across a 10,000-customer
            European banking dataset.
        </div>

        <div class="hero-line"></div>

    </div>

</div>
""")


# =========================================================
# EDITORIAL INTRO
# =========================================================

st.html("""
<div class="editorial-section">

    <div class="editorial-kicker">
        The Analysis
    </div>

    <div class="editorial-title">
        From customer data to business insight.
    </div>

    <div class="editorial-description">
        Explore the patterns behind observed customer churn through
        interactive segmentation, geographic analysis, financial
        exposure analysis and customer-level drill-downs.
    </div>

</div>
""")


# =========================================================
# HEADER
# =========================================================

st.title("Customer Segmentation & Churn Pattern Analytics")
st.caption("European Banking Customer Churn Dashboard")

st.divider()


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Dashboard Filters")

geographies = st.sidebar.multiselect(
    "Geography",
    options=sorted(df["Geography"].unique()),
    default=sorted(df["Geography"].unique())
)

genders = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["Gender"].unique()),
    default=sorted(df["Gender"].unique())
)

activity = st.sidebar.selectbox(
    "Activity Status",
    options=["All", "Active", "Inactive"]
)


# Apply filters

filtered_df = df[
    df["Geography"].isin(geographies)
    & df["Gender"].isin(genders)
].copy()

if activity == "Active":
    filtered_df = filtered_df[
        filtered_df["IsActiveMember"] == 1
    ]

elif activity == "Inactive":
    filtered_df = filtered_df[
        filtered_df["IsActiveMember"] == 0
    ]


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_customers = len(filtered_df)
total_churned = int(filtered_df["Exited"].sum())

if total_customers > 0:
    filtered_churn_rate = churn_rate(filtered_df)
else:
    filtered_churn_rate = 0

high_value = filtered_df[filtered_df["HighValue"]]

if len(high_value) > 0:
    high_value_churn_rate = churn_rate(high_value)
else:
    high_value_churn_rate = 0


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churn Rate",
    f"{filtered_churn_rate:.2f}%"
)

col3.metric(
    "Churned Customers",
    f"{total_churned:,}"
)

col4.metric(
    "High-Value Churn Rate",
    f"{high_value_churn_rate:.2f}%"
)


# =========================================================
# GEOGRAPHY ANALYSIS
# =========================================================

st.subheader("Geographic Churn Analysis")

geo = geographic_risk_index(filtered_df).reset_index()

col1, col2 = st.columns(2)

with col1:

    fig_geo = px.bar(
        geo,
        x="Geography",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Geography"
    )

    fig_geo.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_geo.update_layout(
        yaxis_title="Churn Rate (%)",
        xaxis_title="Geography"
    )

    st.plotly_chart(
        fig_geo,
        width="stretch"
    )


with col2:

    fig_risk = px.bar(
        geo,
        x="Geography",
        y="Risk_Index",
        text="Risk_Index",
        title="Geographic Risk Index"
    )

    fig_risk.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig_risk.update_layout(
        yaxis_title="Risk Index",
        xaxis_title="Geography"
    )

    st.plotly_chart(
        fig_risk,
        width="stretch"
    )


# =========================================================
# AGE ANALYSIS
# =========================================================

st.subheader("Age Segment Analysis")

age = churn_by_group(
    filtered_df,
    "AgeGroup"
).reset_index()

age_order = [
    "Under 30",
    "30-45",
    "46-60",
    "60+"
]

age["AgeGroup"] = pd.Categorical(
    age["AgeGroup"],
    categories=age_order,
    ordered=True
)

age = age.sort_values("AgeGroup")

fig_age = px.bar(
    age,
    x="AgeGroup",
    y="Churn_Rate",
    text="Churn_Rate",
    title="Observed Churn Rate by Age Group"
)

fig_age.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig_age.update_layout(
    yaxis_title="Churn Rate (%)",
    xaxis_title="Age Group"
)

st.plotly_chart(
    fig_age,
    width="stretch"
)


# =========================================================
# TENURE + ACTIVITY
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Tenure Analysis")

    tenure = churn_by_group(
        filtered_df,
        "TenureGroup"
    ).reset_index()

    tenure_order = [
        "New",
        "Mid-term",
        "Long-term"
    ]

    tenure["TenureGroup"] = pd.Categorical(
        tenure["TenureGroup"],
        categories=tenure_order,
        ordered=True
    )

    tenure = tenure.sort_values("TenureGroup")

    fig_tenure = px.bar(
        tenure,
        x="TenureGroup",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Tenure"
    )

    fig_tenure.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_tenure.update_layout(
        yaxis_title="Churn Rate (%)",
        xaxis_title="Tenure"
    )

    st.plotly_chart(
        fig_tenure,
        width="stretch"
    )


with col2:

    st.subheader("Activity Analysis")

    activity_df = churn_by_group(
        filtered_df,
        "IsActiveMember"
    ).reset_index()

    activity_df["Activity"] = activity_df[
        "IsActiveMember"
    ].map({
        0: "Inactive",
        1: "Active"
    })

    fig_activity = px.bar(
        activity_df,
        x="Activity",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Activity"
    )

    fig_activity.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_activity.update_layout(
        yaxis_title="Churn Rate (%)",
        xaxis_title="Activity Status"
    )

    st.plotly_chart(
        fig_activity,
        width="stretch"
    )


# =========================================================
# PRODUCT + CREDIT SCORE ANALYSIS
# =========================================================

st.subheader("Product & Credit Score Analysis")

col1, col2 = st.columns(2)

with col1:

    product = churn_by_group(
        filtered_df,
        "NumOfProducts"
    ).reset_index()

    product["NumOfProducts"] = product[
        "NumOfProducts"
    ].astype(str)

    fig_product = px.bar(
        product,
        x="NumOfProducts",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Number of Products"
    )

    fig_product.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_product.update_layout(
        xaxis_title="Number of Products",
        yaxis_title="Churn Rate (%)"
    )

    st.plotly_chart(
        fig_product,
        width="stretch"
    )


with col2:

    credit = churn_by_group(
        filtered_df,
        "CreditScoreGroup"
    ).reset_index()

    credit_order = [
        "Low",
        "Medium",
        "High"
    ]

    credit["CreditScoreGroup"] = pd.Categorical(
        credit["CreditScoreGroup"],
        categories=credit_order,
        ordered=True
    )

    credit = credit.sort_values("CreditScoreGroup")

    fig_credit = px.bar(
        credit,
        x="CreditScoreGroup",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Credit Score"
    )

    fig_credit.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_credit.update_layout(
        xaxis_title="Credit Score Group",
        yaxis_title="Churn Rate (%)"
    )

    st.plotly_chart(
        fig_credit,
        width="stretch"
    )


# =========================================================
# FINANCIAL + GEOGRAPHIC DEEP-DIVE
# =========================================================

st.subheader("Financial & Geographic Deep-Dive")

st.caption(
    "Descriptive analysis of customer balances, salaries, and "
    "geography-age churn patterns."
)


# ---------------------------------------------------------
# Balance Analysis
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    balance_data = churn_by_group(
        filtered_df,
        "BalanceGroup"
    ).reset_index()

    balance_order = [
        "Zero Balance",
        "Low Balance",
        "High Balance"
    ]

    balance_data["BalanceGroup"] = pd.Categorical(
        balance_data["BalanceGroup"],
        categories=balance_order,
        ordered=True
    )

    balance_data = balance_data.sort_values("BalanceGroup")

    fig_balance = px.bar(
        balance_data,
        x="BalanceGroup",
        y="Churn_Rate",
        text="Churn_Rate",
        title="Observed Churn Rate by Balance Segment"
    )

    fig_balance.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_balance.update_layout(
        xaxis_title="Balance Segment",
        yaxis_title="Churn Rate (%)"
    )

    st.plotly_chart(
        fig_balance,
        width="stretch"
    )


# ---------------------------------------------------------
# Salary vs Balance
# ---------------------------------------------------------

with col2:

    salary_balance = filtered_df.copy()

    salary_balance["Customer Status"] = salary_balance[
        "Exited"
    ].map({
        0: "Retained",
        1: "Churned"
    })

    fig_salary = px.scatter(
        salary_balance,
        x="EstimatedSalary",
        y="Balance",
        color="Customer Status",
        hover_data=[
            "CustomerId",
            "Geography",
            "Age",
            "CreditScore"
        ],
        title="Estimated Salary vs Account Balance"
    )

    fig_salary.update_layout(
        xaxis_title="Estimated Salary",
        yaxis_title="Account Balance"
    )

    st.plotly_chart(
        fig_salary,
        width="stretch"
    )


# ---------------------------------------------------------
# Financial KPIs
# ---------------------------------------------------------

financial_col1, financial_col2, financial_col3 = st.columns(3)

with financial_col1:

    avg_balance_churned = filtered_df.loc[
        filtered_df["Exited"] == 1,
        "Balance"
    ].mean()

    st.metric(
        "Avg Balance · Churned",
        f"€{avg_balance_churned:,.0f}"
    )


with financial_col2:

    avg_balance_retained = filtered_df.loc[
        filtered_df["Exited"] == 0,
        "Balance"
    ].mean()

    st.metric(
        "Avg Balance · Retained",
        f"€{avg_balance_retained:,.0f}"
    )


with financial_col3:

    churned_balance_exposure = filtered_df.loc[
        filtered_df["Exited"] == 1,
        "Balance"
    ].sum()

    st.metric(
        "Churned Balance Exposure",
        f"€{churned_balance_exposure:,.0f}"
    )


# ---------------------------------------------------------
# Geography · Age Analysis
# ---------------------------------------------------------

st.subheader("Geography · Age Churn Pattern")

geo_age = (
    filtered_df
    .groupby(
        ["Geography", "AgeGroup"]
    )["Exited"]
    .mean()
    .reset_index()
)

geo_age["Churn_Rate"] = (
    geo_age["Exited"] * 100
).round(2)

age_order = [
    "Under 30",
    "30-45",
    "46-60",
    "60+"
]

geo_age["AgeGroup"] = pd.Categorical(
    geo_age["AgeGroup"],
    categories=age_order,
    ordered=True
)

geo_age = geo_age.sort_values("AgeGroup")

fig_geo_age = px.bar(
    geo_age,
    x="Geography",
    y="Churn_Rate",
    color="AgeGroup",
    barmode="group",
    text="Churn_Rate",
    title="Observed Churn Rate by Geography and Age Group"
)

fig_geo_age.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig_geo_age.update_layout(
    xaxis_title="Geography",
    yaxis_title="Churn Rate (%)",
    legend_title="Age Group"
)

st.plotly_chart(
    fig_geo_age,
    width="stretch"
)


# =========================================================
# CUSTOMER DRILL-DOWN / HIGH-VALUE EXPLORER
# =========================================================

st.subheader("Customer Drill-Down Explorer")

st.caption(
    "Use this section to inspect individual customer records and "
    "identify high-value customers associated with observed churn."
)

explorer_col1, explorer_col2 = st.columns([1, 2])

with explorer_col1:

    explorer_view = st.selectbox(
        "Customer View",
        [
            "All Customers",
            "Churned Customers",
            "High-Value Customers",
            "High-Value Churners"
        ]
    )


with explorer_col2:

    customer_search = st.text_input(
        "Search Customer ID or Surname",
        placeholder="Example: 15634602 or Smith"
    )


explorer_df = filtered_df.copy()

if explorer_view == "Churned Customers":

    explorer_df = explorer_df[
        explorer_df["Exited"] == 1
    ]

elif explorer_view == "High-Value Customers":

    explorer_df = explorer_df[
        explorer_df["HighValue"] == True
    ]

elif explorer_view == "High-Value Churners":

    explorer_df = explorer_df[
        (explorer_df["HighValue"] == True) &
        (explorer_df["Exited"] == 1)
    ]


if customer_search:

    search_text = customer_search.strip().lower()

    explorer_df = explorer_df[
        explorer_df["CustomerId"].astype(str).str.lower().str.contains(
            search_text,
            na=False
        )
        |
        explorer_df["Surname"].astype(str).str.lower().str.contains(
            search_text,
            na=False
        )
    ]


display_columns = [
    "CustomerId",
    "Surname",
    "Geography",
    "Gender",
    "Age",
    "AgeGroup",
    "CreditScore",
    "CreditScoreGroup",
    "Tenure",
    "TenureGroup",
    "Balance",
    "BalanceGroup",
    "EstimatedSalary",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "HighValue",
    "Exited"
]

display_df = explorer_df[display_columns].copy()

display_df["Status"] = display_df["Exited"].map({
    0: "Retained",
    1: "Churned"
})

display_df["HighValue"] = display_df["HighValue"].map({
    True: "Yes",
    False: "No"
})

display_df["Balance"] = display_df["Balance"].round(2)
display_df["EstimatedSalary"] = display_df["EstimatedSalary"].round(2)

display_df = display_df[
    [
        "CustomerId",
        "Surname",
        "Geography",
        "Gender",
        "Age",
        "CreditScore",
        "Tenure",
        "Balance",
        "EstimatedSalary",
        "NumOfProducts",
        "IsActiveMember",
        "HighValue",
        "Status"
    ]
]

st.write(
    f"Showing **{len(display_df):,}** customer records"
)

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)

csv_data = display_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Customer Data as CSV",
    data=csv_data,
    file_name="customer_drilldown.csv",
    mime="text/csv"
)


# =========================================================
# EXECUTIVE INSIGHTS
# =========================================================

st.subheader("Executive Insights")

st.caption(
    "These insights summarize observed patterns in the currently "
    "selected customer population. They should be interpreted as "
    "associations rather than causal relationships."
)


# Calculate dynamic insights from the filtered dataset

overall_filtered_churn = (
    filtered_df["Exited"].mean() * 100
)

age_analysis = churn_by_group(
    filtered_df,
    "AgeGroup"
)

geo_analysis = churn_by_group(
    filtered_df,
    "Geography"
)

activity_analysis = churn_by_group(
    filtered_df,
    "IsActiveMember"
)

high_value_filtered = filtered_df[
    filtered_df["HighValue"] == True
]

if len(high_value_filtered) > 0:

    high_value_churn_rate = (
        high_value_filtered["Exited"].mean() * 100
    )

else:

    high_value_churn_rate = 0


# Highest observed age segment

highest_age_group = (
    age_analysis["Churn_Rate"].idxmax()
)

highest_age_rate = (
    age_analysis["Churn_Rate"].max()
)


# Highest observed geography

highest_geo = (
    geo_analysis["Churn_Rate"].idxmax()
)

highest_geo_rate = (
    geo_analysis["Churn_Rate"].max()
)


# Activity comparison

if 1 in activity_analysis.index and 0 in activity_analysis.index:

    active_rate = activity_analysis.loc[
        1,
        "Churn_Rate"
    ]

    inactive_rate = activity_analysis.loc[
        0,
        "Churn_Rate"
    ]

else:

    active_rate = None
    inactive_rate = None


insight_col1, insight_col2, insight_col3 = st.columns(3)


with insight_col1:

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:22px;
            border-radius:14px;
            border:1px solid #e2e7ef;
            box-shadow:0 4px 14px rgba(20,30,50,0.06);
            min-height:150px;
        ">

            <div style="
                font-size:14px;
                color:#667085;
                font-weight:600;
                margin-bottom:10px;
            ">
                HIGHEST AGE-SEGMENT CHURN
            </div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:#172033;
            ">
                {highest_age_group}
            </div>

            <div style="
                font-size:18px;
                font-weight:700;
                margin-top:8px;
            ">
                {highest_age_rate:.2f}% observed churn
            </div>

            <div style="
                font-size:13px;
                color:#667085;
                margin-top:8px;
            ">
                Highest observed churn rate among the selected age groups.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with insight_col2:

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:22px;
            border-radius:14px;
            border:1px solid #e2e7ef;
            box-shadow:0 4px 14px rgba(20,30,50,0.06);
            min-height:150px;
        ">

            <div style="
                font-size:14px;
                color:#667085;
                font-weight:600;
                margin-bottom:10px;
            ">
                HIGHEST-GEOGRAPHY CHURN
            </div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:#172033;
            ">
                {highest_geo}
            </div>

            <div style="
                font-size:18px;
                font-weight:700;
                margin-top:8px;
            ">
                {highest_geo_rate:.2f}% observed churn
            </div>

            <div style="
                font-size:13px;
                color:#667085;
                margin-top:8px;
            ">
                Geographic comparison based on the selected population.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with insight_col3:

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:22px;
            border-radius:14px;
            border:1px solid #e2e7ef;
            box-shadow:0 4px 14px rgba(20,30,50,0.06);
            min-height:150px;
        ">

            <div style="
                font-size:14px;
                color:#667085;
                font-weight:600;
                margin-bottom:10px;
            ">
                HIGH-VALUE CHURN RATE
            </div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:#172033;
            ">
                {high_value_churn_rate:.2f}%
            </div>

            <div style="
                font-size:13px;
                color:#667085;
                margin-top:12px;
            ">
                Observed churn among customers classified as high-value
                using the project-defined balance and salary criteria.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# Activity observation

if active_rate is not None:

    st.markdown(
        f"""
        <div style="
            margin-top:18px;
            padding:18px 22px;
            background:white;
            border-left:5px solid #1f77b4;
            border-radius:10px;
            border-top:1px solid #e2e7ef;
            border-right:1px solid #e2e7ef;
            border-bottom:1px solid #e2e7ef;
        ">

            <b>Engagement observation:</b>

            customers classified as inactive show an observed churn rate
            of <b>{inactive_rate:.2f}%</b>, compared with
            <b>{active_rate:.2f}%</b> for active customers in the
            selected population.

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# PROJECT NOTE
# =========================================================

st.markdown(
    """
    <div style="
        margin-top:35px;
        padding:20px;
        background:#eef2f7;
        border-radius:12px;
        text-align:center;
        color:#667085;
        font-size:13px;
    ">

        <b>Pattern Analytics</b><br>

        Customer Segmentation & Churn Pattern Analytics in European Banking

        <br><br>

        All churn metrics represent observed historical patterns in the
        supplied dataset. They are not predictive probabilities and do not
        establish causation.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HIGH-VALUE CUSTOMER ANALYSIS
# =========================================================

st.subheader("High-Value Customer Analysis")

high_value_customers = len(high_value)

high_value_churned = int(
    high_value["Exited"].sum()
)

balance_exposure = high_value.loc[
    high_value["Exited"] == 1,
    "Balance"
].sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "High-Value Customers",
    f"{high_value_customers:,}"
)

col2.metric(
    "High-Value Churned",
    f"{high_value_churned:,}"
)

col3.metric(
    "Churned Balance Exposure",
    f"€{balance_exposure:,.2f}"
)


# =========================================================
# DATA TABLE
# =========================================================

with st.expander("View Geographic Detail"):

    st.dataframe(
        geo,
        width="stretch",
        hide_index=True
    )

st.caption(
    "Note: Churn rates and segment differences are descriptive associations "
    "in the observed dataset and should not be interpreted as causal effects."
)