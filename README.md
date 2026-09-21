# Pattern Analytics: European Banking Customer Intelligence Platform

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-1e293b.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit Framework](https://img.shields.io/badge/Streamlit-1.30%2B-0284c7.svg?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![Plotly Dark](https://img.shields.io/badge/Plotly-Dark_Theme-334155.svg?style=flat-square&logo=plotly)](https://plotly.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL_/_Supabase-0f172a.svg?style=flat-square&logo=postgresql)](https://supabase.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-475569.svg?style=flat-square)](LICENSE)

> A quantitative empirical investigation into retail customer attrition, multi-dimensional segmentation, and capital flight exposure across 10,000 European consumer banking accounts in France, Germany, and Spain.

---

### Author Profile
- **Lead Researcher & Systems Architect:** Panchaksharayya
- **Academic Program:** B.Tech Student in Information Technology (Specialization: Augmented Reality & Virtual Reality)
- **Primary Contact:** [panchaksharayyas22@gmail.com](mailto:panchaksharayyas22@gmail.com)
- **Interactive Dashboard:** [http://localhost:8501](http://localhost:8501) (Streamlit runtime)

---

### Project Deliverables & Working Documents

The table below provides direct download links (which open natively in Microsoft Office) alongside web-based interactive previews:

| Deliverable | Format | Direct Download (Opens in App) | Web Preview / Online Viewer | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Executive Presentation Deck** | `.pptx` (PowerPoint) | [▸ Download Presentation (.pptx)](https://github.com/panchaksharayya12/Pattern_Analytics/raw/main/Pattern_Analytics_Presentation.pptx) | [▸ View in PowerPoint Online](https://view.officeapps.live.com/op/view.aspx?src=https://raw.githubusercontent.com/panchaksharayya12/Pattern_Analytics/main/Pattern_Analytics_Presentation.pptx) · [HTML Web Deck](https://raw.githack.com/panchaksharayya12/Pattern_Analytics/main/reports/presentation_slides.html) | 16-slide widescreen (16:9) executive deck with dark financial palette, KPI scorecards, speaker notes, and literature references. |
| **Technical Enterprise Report** | `.docx` (Word) | [▸ Download Project Report (.docx)](https://github.com/panchaksharayya12/Pattern_Analytics/raw/main/Pattern_Analytics_Project_Report.docx) | [▸ View in Word Online](https://view.officeapps.live.com/op/view.aspx?src=https://raw.githubusercontent.com/panchaksharayya12/Pattern_Analytics/main/Pattern_Analytics_Project_Report.docx) · [HTML Version](https://raw.githack.com/panchaksharayya12/Pattern_Analytics/main/reports/project_report.html) | Comprehensive engineering and consulting document with architecture diagrams, empirical data tables, and 90-day retention roadmap. |
| **Academic Research Paper** | `.docx` (Word) | [▸ Download Research Paper (.docx)](https://github.com/panchaksharayya12/Pattern_Analytics/raw/main/Pattern_Analytics_Research_Paper.docx) | [▸ View in Word Online](https://view.officeapps.live.com/op/view.aspx?src=https://raw.githubusercontent.com/panchaksharayya12/Pattern_Analytics/main/Pattern_Analytics_Research_Paper.docx) · [HTML Version](https://raw.githack.com/panchaksharayya12/Pattern_Analytics/main/reports/research_paper.html) | Publication-format paper styled to IEEE standards with mathematical formulations (GRI, Capital Flight), theorems, and formal citations. |
| **Resume & Interview Toolkit** | `.md` (Markdown) | [▸ View Toolkit (.md)](resume_project_summary.md) | [▸ Markdown Source](resume_project_summary.md) | Copy-paste ATS resume points for Data Analyst and Data Scientist roles, project description, and top 10 technical interview Q&A. |

---

## 1. Executive Summary & Core Empirical Findings

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

### Critical Findings:

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
   - Defecting high-value customers represent only 6.91% of total accounts but account for **€83.38 million (44.9%)** of all liquid capital drained from the institution.

---

## 2. System Architecture & Technical Stack

The application features a decoupled, modular analytics architecture:

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
|   PostgreSQL Cloud Database & Flat Files (sql/)                                   |
|   - sql/schema.sql: Primary table with integrity constraints & B-tree indexes    |
|   - sql/analytics_views.sql: Pre-computed analytical views for rapid reporting    |
|   - src/supabase_client.py: Dual-mode connector with transparent local fallback   |
|   - data/European_Bank.csv: Local flat-file mirror for offline operation          |
+-----------------------------------------------------------------------------------+
```

---

## 3. Repository Directory Structure

```text
Pattern_Analytics/
|-- assets/
|   `-- hero_europe_night.png         # Reference 16:9 cinematic master banner
|-- dashboard/
|   `-- app.py                        # Production Streamlit web application
|-- data/
|   |-- European_Bank.csv             # 10,000-customer benchmark retail dataset
|   `-- customer_data.csv             # Auxiliary customer records mirror
|-- reports/
|   |-- Pattern_Analytics_Presentation.pptx   # 16-slide PowerPoint deck
|   |-- Pattern_Analytics_Project_Report.docx # Word enterprise technical report
|   |-- Pattern_Analytics_Research_Paper.docx # Word IEEE academic research paper
|   |-- presentation_slides.html              # Interactive browser presentation deck
|   |-- project_report.html                   # Styled HTML enterprise report
|   |-- research_paper.html                   # Styled HTML research paper
|   |-- resume_project_summary.md             # Resume bullet points & interview Q&A
|   `-- index.html                            # Master deliverables portal
|-- sql/
|   |-- schema.sql                    # PostgreSQL table DDL & index constraints
|   `-- analytics_views.sql           # Production analytical views (GRI, cohorts)
|-- src/
|   |-- __init__.py
|   |-- data_loader.py                # Ingestion & validation module
|   |-- preprocessing.py              # Cohort binning transformations
|   |-- segmentation.py               # RFM and demographic clustering logic
|   |-- analytics.py                  # Core churn formulas & GRI calculation
|   `-- supabase_client.py            # Database client with local CSV fallback
|-- requirements.txt                  # Pinned Python package dependencies
`-- README.md                         # Project documentation
```

---

## 4. Setup & Local Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/panchaksharayya12/Pattern_Analytics.git
cd Pattern_Analytics
```

### Step 2: Configure Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application
```bash
streamlit run dashboard/app.py
```
Open your browser at [http://localhost:8501](http://localhost:8501).

---

## 5. Interactive Dashboard Architecture

The dashboard comprises five primary analytical modules:

1. **Section 01: Overview (`#overview`)**
   - Portfolio-level KPI scorecards covering total accounts, benchmark defection, high-value attrition rate, and capital liquidity exposure.
2. **Section 02: Sovereign Landscape (`#landscape`)**
   - Cross-border comparative analysis across France, Germany, and Spain.
   - Geographic Risk Index (GRI) benchmarks and capital loss distribution.
   - Demographic gradient analysis (<30, 30–45, 46–60, 60+) and market interaction effects.
3. **Section 03: Customer Patterns (`#patterns`)**
   - Non-linear product bundling curve isolating the 2-product golden anchor vs. 3+ product cliff.
   - Credit score categorization (Low, Medium, High).
   - Digital engagement analysis: active accounts (14.27%) vs. inactive accounts (26.85%).
   - Gender-segmented attrition rates.
4. **Section 04: Financial Risk & Exposure (`#financial-risk`)**
   - Balance strata distribution (Zero Balance, Low Balance, High Balance).
   - Capital flight analysis: average balance comparison between retained (€72k) and churned (€91k) depositors.
   - High-Value Customer ($HVC$) concentration analysis (€83.38M exposure).
5. **Section 05: Customer Stories Explorer (`#customer-stories`)**
   - Granular account search by Customer ID or Surname.
   - Segment-filtered cohort views (All, Churned Only, High-Value Only, High-Value Churners Only).
   - Real-time CSV cohort download for integration into downstream retention systems.

---

## 6. Database Views & SQL Schemas

The database layer includes 7 pre-computed analytical views for rapid reporting:

- `european_bank_customers`: Primary relation with integrity constraints.
- `v_executive_portfolio_summary`: Portfolio aggregate metrics and capital flight totals.
- `v_geographic_risk_index`: Real-time calculation of country risk ratios.
- `v_age_segment_churn`: Demographic cohort attrition statistics.
- `v_product_penetration_risk`: Multi-product holding hazard rates.
- `v_high_value_customer_exposure`: Affluent depositor balance concentration.

---

## 7. Scholarly & Regulatory Citations

1. Boot, A. W. (2000). Relationship banking: What do we know? *Journal of Financial Intermediation*, 9(1), 7–25.
2. Cohen, M. (2004). Customer retention in retail banking: An empirical study of multi-product relationships. *International Journal of Bank Marketing*, 22(4), 254–271.
3. Degryse, H., & Ongena, S. (2007). The impact of technology and regulation on the geography of banking. *Oxford Review of Economic Policy*, 23(2), 265–285.
4. Kim, M., Kliger, D., & Vale, B. (2003). Estimating switching costs: The case of banking. *Journal of Financial Intermediation*, 12(1), 25–56.
5. Klemperer, P. (1995). Competition when consumers have switching costs. *The Review of Economic Studies*, 62(4), 515–539.
6. Modigliani, F. (1986). Life cycle, individual thrift, and the wealth of nations. *The American Economic Review*, 76(3), 297–313.
7. Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools.* Bank for International Settlements (BIS).

---

## 8. License & Terms

- **License:** MIT License. Permitted for research and commercial evaluation.
- **Analytical Disclaimer:** Observed churn rates and segment disparities represent empirical associations derived from historical microdata and serve as diagnostic risk indicators rather than deterministic causal relations.
