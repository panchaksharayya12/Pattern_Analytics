# Pattern Analytics · European Banking Customer Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Dark%20Theme-00d2ff.svg)](https://plotly.com/)
[![Database](https://img.shields.io/badge/PostgreSQL-Supabase-3ECF8E.svg)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Understanding why customers leave:** A comprehensive customer segmentation, churn pattern analytics, and capital flight intelligence platform across a 10,000-customer European retail banking microdataset spanning France, Germany, and Spain.

---

### 👤 Author & Lead Architect
- **Name:** **Panchaksharayya**
- **Academic Degree:** **B.Tech Student in Information Technology (Specialization: Augmented Reality & Virtual Reality)**
- **Email:** **panchaksharayyas22@gmail.com**
- **Live Interactive Dashboard:** **[http://localhost:8501](http://localhost:8501)**

---

### 📂 Institutional Project Deliverables (Direct Downloads):
- 📊 **[PowerPoint Presentation Deck (.pptx)](Pattern_Analytics_Presentation.pptx)** — 16 widescreen slides with dark cinematic palette, KPI cards, presenter notes, and references.
- 📑 **[Technical Enterprise Project Report (.docx)](Pattern_Analytics_Project_Report.docx)** — Complete Word report with system architecture, empirical tables, 90-day retention roadmap, and ATS resume points.
- 🔬 **[Academic Research Paper (.docx)](Pattern_Analytics_Research_Paper.docx)** — IEEE journal formatted paper with mathematical equations for GRI and balance flight, abstract box, and formal citations.
- 💼 **[Resume & Interview Toolkit (.md)](resume_project_summary.md)** — Copy-paste ATS resume bullet points, LinkedIn announcement post, and Top 10 Technical Interview Q&A.


---

## 🌟 Executive Overview & Key Findings

Customer attrition represents one of the largest hidden drags on retail banking balance sheets. `Pattern Analytics` provides executive decision-support and granular behavioral segmentation across demographic, financial, and product dimensions to quantify capital exposure and guide proactive retention strategies.

```
+----------------------------------------------------------------------------------------------------+
|                                      KEY PORTFOLIO BENCHMARKS                                      |
+------------------------------+------------------------------+--------------------------------------+
| TOTAL ANALYZED PORTFOLIO     | BENCHMARK CHURN RATE         | TOTAL BALANCE EXPOSURE AT RISK       |
| 10,000 Customer Accounts     | 20.37% (2,037 Churned)       | €185,588,098                         |
+------------------------------+------------------------------+--------------------------------------+
| HIGH-VALUE CHURN RATE        | HIGH-VALUE CAPITAL FLIGHT    | AVERAGE CHURNER BALANCE              |
| 28.67% (691 Churned HVCs)    | €83,382,307 (44.9% of total) | €91,108 (+25.2% vs Retained Average) |
+------------------------------+------------------------------+--------------------------------------+
```

### Critical Empirical Patterns

1. **The German Geographic Disparity (Risk Index: 1.59):**
   - Germany suffers an acute **32.44% churn rate**—exactly double the rates observed in France (16.15%) and Spain (16.67%).
   - Over **€102.41 million** (55.2% of all lost capital) originated in the German market due to aggressive fee competition from cooperative and public savings banks.
2. **The 46–60 Pre-Retirement Hazard (56.21% Churn):**
   - While younger accounts (under 30) exhibit minimal churn (**7.52%**), customers aged **46 to 60 defect at a staggering 56.21%**.
   - Standard transactional retail checking products fail to meet the wealth preservation, pension consolidation, and estate planning needs of this peak wealth cohort.
3. **The Multi-Product Hazard Curve:**
   - Accounts holding **2 products** form the institutional retention anchor at **7.58% churn**.
   - Cross-selling beyond two products triggers extreme friction: churn surges to **82.71% for 3 products** and reaches **100.00% for 4 products** due to unexpected maintenance fees and service complexity.
4. **The Wealth Paradox in Capital Flight:**
   - Churning accounts hold an average balance of **€91,108** compared to **€72,745** for retained accounts (+25.2% higher).
   - Defecting high-value customers ($Balance > €50k \land Salary > €100k$) represent only 6.91% of total accounts but account for **€83.38 million (44.9%)** of all liquid capital drained from the institution.

---

## 🖥️ System Architecture & UI/UX Design

The application features a modern, dark cinematic aesthetic built directly around the master visual blueprint:

```
+-----------------------------------------------------------------------------------+
|                                PRESENTATION LAYER                                 |
|   Streamlit Interactive Dashboard (dashboard/app.py)                              |
|   - Base64 Master Hero Frame with Clickable Transparent Hotspots                  |
|   - Sticky Floating Sub-Navigation Bar (#overview, #landscape, #patterns, etc.)   |
|   - Glassmorphic KPI Cards with Top-Border Accent Glows                           |
|   - Plotly Dark High-Contrast Visualizations with Custom Palette                  |
|   - Real-Time Dynamic Sidebar Filtering (Market, Gender, Member Activity)        |
|   - Granular Customer Stories Drill-Down Explorer with One-Click CSV Export       |
+-----------------------------------------------------------------------------------+
                                          ▲
                                          │
+-----------------------------------------------------------------------------------+
|                                 ANALYTICAL ENGINE                                 |
|   Python Core Analytics Engine (src/)                                             |
|   - src/data_loader.py: Data ingestion & validation                               |
|   - src/preprocessing.py: Non-linear age cohort binning (<30, 30-45, 46-60, 60+)  |
|   - src/segmentation.py: Multi-dimensional segmentation & High-Value classification|
|   - src/analytics.py: Churn rates, Geographic Risk Index (GRI), financial exposure|
+-----------------------------------------------------------------------------------+
                                          ▲
                                          │
+-----------------------------------------------------------------------------------+
|                             DATA & PERSISTENCE LAYER                              |
|   Supabase / PostgreSQL Cloud Database (sql/)                                     |
|   - sql/schema.sql: Primary table with integrity constraints & B-tree indexes    |
|   - sql/analytics_views.sql: Pre-computed analytical views for rapid reporting    |
|   - src/supabase_client.py: Dual-mode connector with transparent local fallback   |
|   - data/European_Bank.csv: Local flat-file mirror for offline operation          |
+-----------------------------------------------------------------------------------+
```

---

## 📁 Repository Structure

```bash
Pattern_Analytics/
│
├── assets/
│   └── hero_europe_night.png         # Reference 16:9 cinematic master banner
│
├── dashboard/
│   └── app.py                        # Main production Streamlit web application
│
├── data/
│   ├── European_Bank.csv             # 10,000-customer benchmark retail dataset
│   └── customer_data.csv             # Auxiliary customer records mirror
│
├── reports/
│   ├── research_paper.md             # Publication-grade academic research paper
│   ├── project_report.md             # Detailed technical & consulting report
│   ├── executive_summary.md          # C-Suite / Board of Directors 2-page briefing
│   └── presentation_deck.md          # 15-slide executive presentation deck
│
├── sql/
│   ├── schema.sql                    # PostgreSQL/Supabase table DDL, constraints & indexes
│   └── analytics_views.sql           # Production analytical views (GRI, age, products)
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py                # Dataset loader module
│   ├── preprocessing.py              # Age cohort binning transformation
│   ├── segmentation.py               # Multi-dimensional customer segmentation
│   ├── analytics.py                  # Core churn metrics & exposure formulations
│   └── supabase_client.py            # Supabase database client with local CSV fallback
│
├── .env.example                      # Environment variables template
├── requirements.txt                  # Pinned Python package dependencies
└── README.md                         # Comprehensive platform documentation
```

---

## 🚀 Quickstart & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Pattern_Analytics.git
cd Pattern_Analytics
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional for Supabase)
Copy `.env.example` to `.env` if connecting to a live Supabase instance:
```bash
cp .env.example .env
```
*(Note: If Supabase credentials are not provided, the platform automatically and transparently operates using local high-performance CSV caching).*

### 5. Launch the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
Open your browser at `http://localhost:8501`.

---

## 📊 Interactive Dashboard Modules

The dashboard features five core interactive analytical modules:

1. **🧭 Overview (`#overview`):**
   - High-level executive KPI scorecard displaying analyzed accounts, observed churn percentage, high-value attrition rate, and total capital exposure.
2. **🌐 Landscape (`#landscape`):**
   - Sovereign market comparisons across Germany, France, and Spain.
   - Geographic Risk Index ($GRI$) benchmarks and country-specific capital flight.
   - Non-linear age gradient analysis (<30, 30–45, 46–60, 60+) and cross-market interaction dynamics.
3. **🧬 Customer Patterns (`#patterns`):**
   - The non-linear product bundling hazard curve (identifying the 2-product golden anchor vs. 3+ product churn hazard).
   - Credit score tier distributions (Low, Medium, High).
   - Active vs. Inactive account engagement disparity (+88.2% churn multiplier).
   - Gender-segmented attrition rates.
4. **💶 Financial Risk (`#financial-risk`):**
   - Balance tier churn distributions (Zero Balance, Low Balance, High Balance).
   - Interactive Estimated Salary vs. Account Balance scatter plot with individual metadata tooltips.
   - Capital flight analysis: average balance comparison between retained (€72k) and churned (€91k) accounts.
   - High-Value Customer ($HVC$) capital concentration deep-dive (€83.38M exposure).
5. **👤 Customer Stories (`#customer-stories`):**
   - Individual customer drill-down explorer with real-time text search by Customer ID or Surname.
   - Pre-filtered cohort views: *All Accounts*, *Churned Accounts Only*, *High-Value Accounts*, *High-Value Churners Only*.
   - One-click CSV cohort export for immediate handoff to regional relationship managers.
   - Dynamic executive synthesis and priority recommendations.

---

## 🗄️ Database & Analytical SQL Views

Execute `sql/schema.sql` and `sql/analytics_views.sql` inside the Supabase SQL Editor or any PostgreSQL database to instantiate:

- `european_bank_customers`: Primary table with foreign keys, check constraints, and performance indexes.
- `v_executive_portfolio_summary`: Portfolio aggregate metrics.
- `v_geographic_risk_index`: Real-time calculation of sovereign risk indices.
- `v_age_segment_churn`: Age cohort churn breakdown.
- `v_product_penetration_risk`: Product holding hazard curve analysis.
- `v_high_value_customer_exposure`: Capital flight tracking among high-balance accounts.

---

## 📄 Comprehensive Deliverables & Documentation

This repository contains institutional-grade reports ready for stakeholder distribution:

- [📘 Academic Research Paper (reports/research_paper.md)](reports/research_paper.md): Full publication-format paper with literature review, empirical theorems, statistical tables, and academic citations.
- [📑 Enterprise Project Report (reports/project_report.md)](reports/project_report.md): Technical architecture, data pipeline, and 90-day operational roadmap.
- [📊 Executive Summary (reports/executive_summary.md)](reports/executive_summary.md): 2-page C-Suite and Board briefing.
- [🎯 Executive Presentation Deck (reports/presentation_deck.md)](reports/presentation_deck.md): Complete 15-slide presentation deck with speaker notes and visual blueprints.

---

## ⚖️ License & Disclaimer

- **License:** MIT License. Free for commercial and research applications.
- **Methodology Disclaimer:** All observed churn metrics and segment differences represent empirical associations within historical microdata. They serve as diagnostic risk indicators rather than deterministic causal relationships.
