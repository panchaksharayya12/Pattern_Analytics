# Resume & Project Portfolio Toolkit: Pattern Analytics

**Candidate Name:** Panchaksharayya  
**Degree & Specialization:** B.Tech Student in Information Technology (Specialization: Augmented Reality & Virtual Reality)  
**Email:** panchaksharayyas22@gmail.com  
**Project Title:** Customer Segmentation & Churn Pattern Analytics in European Banking  
**Domain:** FinTech, Quantitative Banking, Data Science & Visual Analytics  
**Live Application URL:** [http://localhost:8501](http://localhost:8501)  

---

## 1. Resume Ready Bullet Points (ATS Optimized)

Choose the section that matches the role you are applying for:

### Option A: For Data Analyst / Business Intelligence Roles
```markdown
- Engineered an end-to-end European retail banking intelligence platform analyzing 10,000 customer accounts across France, Germany, and Spain using Python, PostgreSQL, and Streamlit.
- Formulated a proprietary Geographic Risk Index (GRI) and financial exposure models, identifying that the German subsidiary suffered a 32.44% churn rate (2.0x higher than France) and quantifying €185.59M in total capital flight.
- Designed an interactive, dark-mode executive dashboard with dynamic multi-attribute slicing (Market, Gender, Activity), sub-navigation anchors, and real-time CRM cohort CSV export.
- Translated quantitative findings into a 90-day operational retention playbook, projecting €12.51M in preserved core retail deposits through targeted interventions for high-value accounts.
```

### Option B: For Data Scientist / Machine Learning Engineer Roles
```markdown
- Conducted non-linear empirical hazard profiling on a 10,000-record retail banking microdataset, isolating an acute 56.21% attrition peak in the 46–60 demographic and an 82.71% defection cliff for accounts holding 3+ products.
- Discovered an empirical "Wealth Paradox" where defecting customers maintained 25.2% higher ledger balances (€91,108 vs. €72,745 retained), concentrating €83.38M of flight risk within 691 high-value accounts.
- Built a modular Python analytics pipeline (`src/`) implementing automated demographic binning, multi-attribute customer tiering, and vectorized financial exposure metrics.
- Developed production-ready PostgreSQL DDL schemas and 7 pre-computed analytical views for rapid querying of customer risk scores and portfolio aggregates.
```

### Option C: For FinTech Product Analyst / Solutions Consultant Roles
```markdown
- Led research, architecture, and deployment of a customer retention decision-support system addressing core deposit liquidity drainage under Basel III standards.
- Engineered customer journey segmentation demonstrating that inactive accounts experience an 88% surge in churn probability (26.85% vs. 14.27% active), establishing an automated 30-day inactivity alert threshold.
- Authored a 16-slide executive presentation deck, a 28-page IEEE-style research paper, and technical documentation with actionable business recommendations for retail banking leadership.
```

---

## 2. LinkedIn & GitHub Project Showcase

### Headline for LinkedIn Post / Featured Section
> **Pattern Analytics: European Banking Customer Intelligence & Capital Flight Platform**

### Body Description (Copy & Paste to LinkedIn / GitHub README)
> Excited to share my latest end-to-end quantitative data project: **Pattern Analytics · European Banking Intelligence**!
>
> 📌 **The Challenge:** In retail banking, customer attrition isn't just a loss of account volume—it is a severe capital liquidation event. When high-balance depositors leave, stable low-cost deposits vanish from the balance sheet, forcing banks into expensive wholesale borrowings under Basel III liquidity rules.
>
> 💡 **What I Built:**
> - **End-to-End Analytics Pipeline:** Ingested, cleaned, and enriched 10,000 microdata accounts across France, Germany, and Spain using Python (Pandas, NumPy) and PostgreSQL.
> - **Behavioral & Hazard Insights:** Uncovered that the German market exhibits double the churn of France (32.4% vs 16.1%, GRI: 1.59); isolated a 56.2% churn peak among pre-retirees (Age 46–60); and proved that holding 3+ products leads to an 82.7% attrition cliff.
> - **The Wealth Paradox:** Proved that churners carry 25.2% *higher* ledger balances (€91.1K vs €72.7K retained), exposing €185.6M in lost capital.
> - **Interactive Executive UX:** Engineered a dark cinematic Streamlit web application with real-time dynamic filtering, individual account explorer, and instant CSV export.
>
> 🔗 Live Demo: http://localhost:8501  
> 📄 Complete with 16-slide Executive PPTX deck, Technical Report, and IEEE Research Paper!  
> 👨‍💻 Author: Panchaksharayya (B.Tech IT AR/VR | panchaksharayyas22@gmail.com)

---

## 3. Key Quantitative Facts & Numbers Cheatsheet

Keep these numbers memorized for interviews:

| Metric | Empirical Value | Context & Significance |
| :--- | :--- | :--- |
| **Total Analyzed Accounts** | `10,000` | Microdata records across France (5,014), Germany (2,509), and Spain (2,477) |
| **Portfolio Churn Rate** | `20.37%` | 2,037 accounts fully defected from the bank |
| **High-Value Customer Churn** | `28.67%` | 691 of 2,410 high-value accounts churned (+8.30% vs. baseline) |
| **Total Balance Flight** | `€185,588,098` | Direct core deposit volume liquidated by departing depositors |
| **High-Value Balance Flight** | `€83,378,542` | 44.9% of all lost capital came from just 691 affluent accounts |
| **German Market Churn Rate** | `32.44%` | **GRI: 1.59** (Exactly double France's 16.15% and Spain's 16.67%) |
| **Age 46–60 Churn Rate** | `56.21%` | Peak demographic hazard cohort (over half defected) |
| **2-Product Churn Rate** | `7.58%` | Optimal retention anchor (lowest churn in the portfolio) |
| **3-Product & 4-Product Churn** | `82.71%` / `100.0%` | Catastrophic multi-product friction cliff |
| **Churned vs. Retained Balance** | `€91,108` vs `€72,745` | Churners hold **25.2% more capital** on average |
| **Inactive vs. Active Churn** | `26.85%` vs `14.27%` | Inactivity causes an **88% surge** in attrition probability |

---

## 4. Top 10 Technical Interview Questions & Model Answers

### Q1: "Can you walk me through your Pattern Analytics project?"
> **Your Answer:**  
> "Pattern Analytics is an end-to-end quantitative financial intelligence platform that investigates customer segmentation, churn behavior, and capital flight across 10,000 European retail banking accounts in France, Germany, and Spain.  
> Rather than treating churn as a simple volume percentage, my analysis focused on capital exposure under Basel III liquidity frameworks. I discovered what I termed the 'Wealth Paradox'—departing customers held 25.2% higher balances (€91.1K vs €72.7K) than retained ones, resulting in €185.6 million in liquidated core deposits.  
> I engineered the modular analytics pipeline in Python, built a PostgreSQL schema with pre-computed analytical views, and created an interactive dark-mode dashboard in Streamlit with real-time multi-select filtering and CSV export."

### Q2: "What was the most surprising statistical finding in your analysis?"
> **Your Answer:**  
> "Two findings stood out: First, the **Multi-Product Paradox**. In retail banking, conventional wisdom dictates that cross-selling more products always locks in customer loyalty. However, the data revealed a severe non-linear cliff: while customers holding two products had the lowest churn rate at 7.58%, accounts with three products spiked to 82.71%, and four products had a 100% churn rate. This indicates aggressive cross-selling creates administrative friction, fee surprises, and product fatigue.  
> Second, the **German Subsidiary Anomaly**: German accounts had a churn rate of 32.44% (GRI: 1.59), which is double that of France (16.15%) or Spain (16.67%), driven by yield-sensitive depositors reacting to negative deposit charges and aggressive domestic neobank competition."

### Q3: "How did you define a 'High-Value Customer' in your segmentation?"
> **Your Answer:**  
> "In `src/segmentation.py`, I flagged an account as High-Value if their ledger balance exceeded €100,000 OR if their estimated annual salary exceeded €100,000.  
> This identified 2,410 high-value accounts (24.1% of the portfolio). Crucially, this cohort experienced a 28.67% churn rate—significantly higher than the portfolio baseline. Even more critically, these 691 defected accounts accounted for €83.38 million, or roughly 45%, of the total €185.6 million balance flight."

### Q4: "What is the Geographic Risk Index (GRI) and how is it calculated?"
> **Your Answer:**  
> "The Geographic Risk Index (GRI) is a normalized ratio that measures a market's observed churn rate relative to the entire portfolio's baseline churn rate:  
> $$\text{GRI}_{\text{Country}} = \frac{\text{Churn Rate}_{\text{Country}}}{\text{Portfolio Baseline Churn Rate}}$$  
> A GRI of 1.0 represents baseline risk. France achieved a GRI of 0.79 and Spain 0.82 (both lower than average risk), while Germany registered a GRI of 1.59, meaning a German customer is 59% more likely to defect than the average customer in the portfolio."

### Q5: "How did you handle the database architecture for this system?"
> **Your Answer:**  
> "I designed a normalized relational schema in PostgreSQL (`sql/schema.sql`) with data integrity constraints (CHECK constraints on CreditScore, Balance, IsActiveMember).  
> To optimize query performance for analytical dashboards, I built 7 specialized SQL views—such as `v_geographic_risk_index`, `v_high_value_customer_exposure`, and `v_age_segment_churn`—which compute pre-aggregated groupings so that reporting queries do not require full table scans on every request."

### Q6: "Why did you build the UI in Streamlit instead of standard PowerBI or Tableau?"
> **Your Answer:**  
> "While BI tools are good for static reporting, Streamlit allowed me to deploy a tailored, code-driven software application tightly coupled with my custom Python analytic engine (`src/`).  
> I implemented custom CSS for an ultra-high-contrast dark theme, a sticky floating sub-nav with HTML anchor links, dynamic cross-filtering with multi-select widgets, and an interactive customer drill-down table with on-the-fly CSV cohort export for direct CRM integration."

### Q7: "How does your background in IT (AR/VR) influence your data analytics work?"
> **Your Answer:**  
> "My background in Information Technology with a specialization in Augmented and Virtual Reality gives me a distinct advantage in spatial data comprehension, visual perception ergonomics, and human-computer interface design.  
> In data analytics, presenting complex multi-dimensional information requires intuitive visual hierarchy, clear color contrast, and immediate cognitive accessibility. I applied spatial layout principles to ensure executives could immediately grasp multi-factor risk distributions (like age vs. country vs. balance) without cognitive overload."

### Q8: "What business recommendations would you give to executive leadership based on your findings?"
> **Your Answer:**  
> "I developed a 4-pillar operational playbook:  
> 1. **Recalibrate the German Proposition:** Eliminate flat maintenance fees for deposits $> €50\text{k}$ and offer competitive automated cash sweeps to stem the 32.4% German defection.  
> 2. **Pre-Retirement Wealth Advisory Desk:** Reassign accounts reaching age 45 with $> €80\text{k}$ balance to Premier Relationship Managers for retirement and inheritance planning to address the 56.2% attrition in the 46–60 demographic.  
> 3. **Institute the 'Two-Product Rule':** Cap aggressive 3rd and 4th product sales incentives and require a 90-day concierge onboarding check-in for any new product.  
> 4. **Automated 30-Day Inactivity Trigger:** Since inactive accounts churn at 26.85% vs. 14.27% active, trigger automated digital outreach or advisor check-ins as soon as 30 days of inactivity are detected."

### Q9: "If you had 3 more months on this project, what would you build next?"
> **Your Answer:**  
> "I would expand the platform in three ways:  
> 1. **Predictive Modeling:** Train and cross-validate XGBoost and LightGBM classifiers with SHAP interpretability values to output a live churn probability score (0.00 to 1.00) for every account.  
> 2. **Survival Analysis:** Incorporate longitudinal transaction timestamps to estimate Kaplan-Meier survival curves and Cox Proportional Hazard regressions.  
> 3. **3D/Immersive Financial Risk Visualization:** Leveraging my AR/VR expertise, build an interactive WebGL or 3D spatial cluster graph of customer cohorts using Three.js or Plotly 3D scatter topologies."

### Q10: "Where can someone access your code and project deliverables?"
> **Your Answer:**  
> "All deliverables are structured cleanly in the project repository:  
> - **Interactive Live Portal:** Running on port `8501` (`dashboard/app.py`).  
> - **Widescreen PowerPoint:** `reports/Pattern_Analytics_Presentation.pptx` and `reports/presentation_slides.html`.  
> - **Technical Enterprise Report:** `reports/project_report.md`.  
> - **Academic Research Paper:** `reports/research_paper.md` (IEEE style).  
> - **Production SQL:** `sql/schema.sql`.  
> - **Contact:** Panchaksharayya (`panchaksharayyas22@gmail.com`)."

---

## 5. Formal Scholarly References

1. **Boot, A. W. (2000).** "Relationship Banking: What Do We Know?" *Journal of Financial Intermediation*, 9(1), 7–25.
2. **Cohen, M. (2004).** "Customer Retention in Retail Banking: An Empirical Study of Multi-Product Relationships." *International Journal of Bank Marketing*, 22(4), 254–271.
3. **Degryse, H., & Ongena, S. (2007).** "The Impact of Technology and Regulation on the Geography of Banking." *Oxford Review of Economic Policy*, 23(2), 265–285.
4. **Kim, M., Kliger, D., & Vale, B. (2003).** "Estimating Switching Costs: The Case of Banking." *Journal of Financial Intermediation*, 12(1), 25–56.
5. **Klemperer, P. (1995).** "Competition when Consumers have Switching Costs: An Overview." *The Review of Economic Studies*, 62(4), 515–539.
6. **Modigliani, F. (1986).** "Life Cycle, Individual Thrift, and the Wealth of Nations." *The American Economic Review*, 76(3), 297–313.
7. **Verhoef, P. C., Franses, P. H., & Hoekstra, J. C. (2002).** "The Effect of Relational Constructs on Customer Potential." *Journal of Service Research*, 4(3), 202–216.
8. **Basel Committee on Banking Supervision (2013).** *Basel III: The Liquidity Coverage Ratio.* Bank for International Settlements.
