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
df = add_segments(df)


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
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 1]

elif activity == "Inactive":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 0]


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

    st.plotly_chart(fig_geo, width="stretch")


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

    st.plotly_chart(fig_risk, width="stretch")


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

st.plotly_chart(fig_age, width="stretch")


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

    st.plotly_chart(fig_tenure, width="stretch")


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

    st.plotly_chart(fig_activity, width="stretch")


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

    product["NumOfProducts"] = product["NumOfProducts"].astype(str)

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

    st.plotly_chart(fig_product, width="stretch")


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

    st.plotly_chart(fig_credit, width="stretch")

# =========================================================
# HIGH-VALUE CUSTOMER ANALYSIS
# =========================================================

st.subheader("High-Value Customer Analysis")

high_value_customers = len(high_value)
high_value_churned = int(high_value["Exited"].sum())

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


